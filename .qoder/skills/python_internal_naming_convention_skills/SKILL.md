---
name: python_internal_naming_convention_skills
description: 当用户要求重构、审查或编写 Python 代码时，请参考此规范检查函数注释和命名约定。
trigger: 重构、审查 Python 代码、编写 Python 函数、commit 前检查
---

# Python 内部命名约定与注释规范

## 核心规则

### 1. 函数/方法注释要求

**所有函数和方法必须添加注释**，使用 docstring 格式：

```python
def function_name(param1, param2):
    """简短描述函数功能。
    
    详细描述（可选）：说明函数的具体行为、边界条件等。
    
    Args:
        param1: 参数 1 的描述
        param2: 参数 2 的描述
    
    Returns:
        返回值的描述
    
    Raises:
        ValueError: 何时抛出此异常
    """
    pass
```

**简化版（单行即可说明清楚时）：**
```python
def get_user_name(user_id):
    """根据用户 ID 获取用户名。"""
    return users[user_id]
```

### 2. 命名约定

| 类型 | 约定 | 示例 |
|------|------|------|
| 模块/文件 | 小写 + 下划线 | `user_manager.py` |
| 类 | 大驼峰 (PascalCase) | `class UserManager:` |
| 函数/方法 | 小写 + 下划线 | `def get_user_info():` |
| 变量 | 小写 + 下划线 | `user_count` |
| 常量 | 全大写 + 下划线 | `MAX_RETRY_COUNT = 5` |
| 私有成员 | 单下划线前缀 | `_internal_helper()` |
| 名称修饰 | 双下划线前缀 | `__private_attr` |

### 3. 代码审查检查清单

在执行以下操作前，必须检查此规范：
- [ ] 所有函数/方法都有 docstring 注释
- [ ] 命名符合上述约定
- [ ] 参数有说明（超过 2 个参数时）
- [ ] 返回值有说明（非 None 返回值）

## 执行流程

当触发此 skill 时：

1. **扫描目标文件**：识别所有函数/方法定义
2. **检查注释**：标记缺少 docstring 的函数
3. **检查命名**：标记不符合命名约定的标识符
4. **生成报告**：列出所有不符合项
5. **提供修复建议**：给出具体修改代码

## 输出格式

发现问题时，按以下格式报告：

```
## 注释规范检查结果

### ❌ 缺少注释的函数
- `file.py:line` - `function_name`: 缺少 docstring

### ⚠️ 命名不规范
- `file.py:line` - `BadName`: 应改为 `good_name`

### 建议修改
```python
# 修改前后的代码对比
```
```

## commit 前检查

当执行 `claude commit` 时，自动触发此检查：
1. 获取变更文件列表
2. 检查所有修改/新增的 Python 函数
3. 如有不符合项，先提示修复再提交

## 示例

**不符合规范的代码：**
```python
def calc(a, b):
    return a + b

class userInfo:
    def getData(self):
        pass
```

**符合规范的代码：**
```python
def calculate_sum(a, b):
    """计算两个数的和。"""
    return a + b

class UserInfo:
    def get_data(self):
        """获取用户数据。"""
        pass
```
