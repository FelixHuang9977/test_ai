#!/usr/bin/env python3
import click
import pytest
import os
import sys
from pathlib import Path

# 定義上下文對象來共享狀態
class Context:
    def __init__(self):
        self.verbose = False
        self.test_dir = "testcase"

# 創建一個 pass_context 裝飾器
pass_context = click.make_pass_decorator(Context, ensure=True)

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--test-dir', default='testcase', help='Test case directory')
@pass_context
def cli(ctx, verbose, test_dir):
    """Diagnostic CLI tool for system testing"""
    ctx.verbose = verbose
    ctx.test_dir = test_dir

@cli.command()
@click.option('--category', help='Filter test cases by category (e.g., cpu)')
@pass_context
def list(ctx, category):
    """List all available test cases"""
    testcase_dir = Path(ctx.test_dir)
    
    if ctx.verbose:
        click.echo(f"Scanning directory: {testcase_dir}")
    
    click.echo("Available test cases:")
    click.echo("===================")
    
    for root, dirs, files in os.walk(testcase_dir):
        # 如果指定了類別，只顯示該類別的測試
        if category and not any(d.startswith(category) for d in Path(root).parts):
            continue
            
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                rel_path = Path(root).relative_to(testcase_dir)
                test_path = rel_path / file
                
                if ctx.verbose:
                    click.echo(f"\nProcessing file: {test_path}")
                
                try:
                    with open(Path(root) / file, 'r') as f:
                        content = f.read()
                        test_methods = [line.strip() for line in content.split('\n') if line.strip().startswith('def test_')]
                    click.secho(f"\n📁 {test_path}:", fg='green')
                    for method in test_methods:
                        method_name = method.split('def ')[1].split('(')[0]
                        click.echo(f"  ▶️  {method_name}")
                        
                except Exception as e:
                    click.secho(f"Error processing {file}: {e}", fg='red')

@cli.command()
@click.argument('test_path', required=False)
@click.option('--stress', is_flag=True, help='Run stress tests')
@click.option('--junit-xml', help='Generate junit-xml report')
@pass_context
def run(ctx, test_path, stress, junit_xml):
    """Run specified test cases"""
    args = []
    
    if ctx.verbose:
        args.append('-v')
    
    if not stress:
        args.append('-m not stress')
    
    if junit_xml:
        args.append(f'--junit-xml={junit_xml}')
    
    if test_path:
        args.append(test_path)
    else:
        args.append(ctx.test_dir)
    
    if ctx.verbose:
        click.echo(f"Running pytest with arguments: {args}")
    
    exit_code = pytest.main(args)
    
    # 使用不同顏色顯示測試結果
    if exit_code == 0:
        click.secho("All tests passed!", fg='green')
    else:
        click.secho("Some tests failed!", fg='red')
    
    sys.exit(exit_code)

@cli.group()
def config():
    """Configuration related commands"""
    pass

@config.command()
@click.option('--output', type=click.Path(), help='Output file for test configuration')
@pass_context
def show(ctx, output):
    """Show current configuration"""
    config_info = {
        "test_directory": ctx.test_dir,
        "verbose_mode": ctx.verbose
    }
    
    if output:
        import json
        with open(output, 'w') as f:
            json.dump(config_info, f, indent=2)
        click.echo(f"Configuration saved to {output}")
    else:
        click.echo("\nCurrent Configuration:")
        for key, value in config_info.items():
            click.echo(f"{key}: {value}")

if __name__ == '__main__':
    cli()
