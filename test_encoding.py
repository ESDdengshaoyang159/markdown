#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编码测试脚本
用于测试文件管理器的编码处理功能
"""

import os
import sys
sys.path.append('src')

from src.core.file_manager import FileManager

def create_test_files():
    """创建不同编码的测试文件"""
    test_dir = "test_files"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # 测试内容
    content = """# 测试标题

这是一个测试文档，包含中文内容。

## 功能测试

- 编码检测
- 文件读取
- 乱码处理

### 特殊字符

中文：你好世界
英文：Hello World
数字：123456
符号：！@#￥%……&*（）
"""
    
    # 创建不同编码的文件
    encodings = {
        'utf-8': 'test_utf8.md',
        'gbk': 'test_gbk.md',
        'utf-8-sig': 'test_utf8_bom.md',
        'gb2312': 'test_gb2312.md'
    }
    
    for encoding, filename in encodings.items():
        filepath = os.path.join(test_dir, filename)
        try:
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(content)
            print(f"创建文件: {filepath} (编码: {encoding})")
        except Exception as e:
            print(f"创建文件失败 {filepath}: {e}")

def test_encoding_detection():
    """测试编码检测功能"""
    print("\n=== 编码检测测试 ===")
    
    file_manager = FileManager()
    test_dir = "test_files"
    
    if not os.path.exists(test_dir):
        print("测试文件目录不存在，请先运行 create_test_files()")
        return
    
    for filename in os.listdir(test_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(test_dir, filename)
            detected_encoding = file_manager.detect_encoding(filepath)
            print(f"文件: {filename}")
            print(f"  检测到的编码: {detected_encoding}")
            
            # 尝试读取文件
            content = file_manager.read_file(filepath)
            if content:
                print(f"  读取成功，内容长度: {len(content)} 字符")
                # 显示前50个字符
                preview = content[:50].replace('\n', '\\n')
                print(f"  内容预览: {preview}...")
            else:
                print(f"  读取失败")
            print()

def main():
    """主函数"""
    print("编码处理测试工具")
    print("1. 创建测试文件")
    print("2. 测试编码检测")
    print("3. 全部测试")
    
    choice = input("请选择操作 (1-3): ").strip()
    
    if choice == '1':
        create_test_files()
    elif choice == '2':
        test_encoding_detection()
    elif choice == '3':
        create_test_files()
        test_encoding_detection()
    else:
        print("无效选择")

if __name__ == '__main__':
    main()