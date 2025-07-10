#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown文件读取器
主程序入口文件
"""

import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(
    os.path.dirname(__file__),
    ".venv", "Lib", "site-packages", "PyQt5", "Qt", "plugins", "platforms"
)
import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    """主函数"""
    app = QApplication(sys.argv)

    # 设置应用程序信息
    app.setApplicationName("Markdown Reader")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("MarkdownReader")

    # 创建主窗口
    window = MainWindow()
    window.show()

    # 运行应用程序
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
