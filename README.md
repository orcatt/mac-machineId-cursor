# mac-machineId-cursor

通过随机修改 macOS 设备的机器标识符，实现 cursor 的无限试用。

## 特性

- 随机修改 `storage.json` 文件中的 `macMachineId`、`machineId` 和 `devDeviceId` 字段。
- 自动跳过空的标识符字段。
- 适用于 macOS 系统的设备信息修改。
- 脚本简单，易于使用。

## 安装与使用

### 安装

1. 克隆仓库或下载 Python 脚本：

```bash
git clone https://github.com/orcatt/mac-machineId-cursor.git
cd mac-machineId-cursor
```

### 基础环境

确保你安装了 Python 3 环境。如果没有安装，可以参考官方文档进行安装。

### 使用

```bash
python modify_mac_ids.py
```

## 脚本内容

脚本将对 storage.json 文件中的以下字段进行修改：

telemetry.sqmId
telemetry.macMachineId
telemetry.machineId
telemetry.devDeviceId
每个字段的值将随机替换其中的两个字符，确保修改后仍符合机器标识符格式。

贡献
欢迎提出改进建议！如果你有好的功能想法或发现了 bug，欢迎提交 issue 或者 pull request。

License
MIT License.
