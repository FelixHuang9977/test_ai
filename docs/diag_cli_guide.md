# Diag CLI 工具指南

## 簡介

diag_cli 是一個系統診斷命令列工具，用於執行系統分析、效能監控和問題診斷。本指南詳細說明工具的使用方法、所有可用命令及其範例。

## 安裝

### 系統需求
- Python 3.6 或更高版本
- Linux/Unix 系統
- root 或 sudo 權限（部分功能需要）
### 安裝步驟
```bash
pip install diag-cli
```
[前面的內容保持不變...]

## USB 測試功能

### 1. 列出 USB 測試案例

命令：
```bash
diag_cli usb list