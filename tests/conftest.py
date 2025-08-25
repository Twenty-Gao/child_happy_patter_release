import pytest
import sys
import os
import asyncio

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 在Windows上设置事件循环策略以避免警告
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import Base
from db.init_db import init_db
from main import app
from fastapi.testclient import TestClient

# 添加pytest asyncio配置
pytest_plugins = ["pytest_asyncio"]

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """在测试会话开始前初始化数据库"""
    # 初始化数据库表
    init_db()
    yield

@pytest.fixture(scope="function")
def client():
    """创建测试客户端"""
    with TestClient(app) as c:
        yield c