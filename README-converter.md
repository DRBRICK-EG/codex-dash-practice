# WooCommerce → GNT 订单转换工具

本地浏览器工具，支持所提供的 WooCommerce XLSX 格式和 GNT 28 列 XLS 模板。

## 运行

在本项目目录执行（需要 Python 3.10 或以上）：

```sh
python -m venv .venv
# macOS / Linux
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
# Windows 改用 .venv\Scripts\python.exe
```

在运行工具的同一台电脑，用浏览器打开 `http://127.0.0.1:8765`。
上传 XLSX，填写寄件资料并应用，逐笔补齐收件区域，核对后下载 XLS。
云端启动并不代表自己的电脑可以访问该地址。

## 转换规则与限制

- 一笔订单一行，仅转换 processing / wc-processing 状态；其他状态明确提示跳过。重复编号、退款订单、非埃及订单拒绝转换。
- 有配送街道时使用整套配送地址；否则使用账单地址。电话优先 shipping_phone，缺失时使用 billing_phone。
- 电话保留文本，不擅自补零。源文件数字电话会提示检查。
- EGGZ → الجيزة，EGC → القاهرة；其他代码须手动选择模板中的省。城市仅在对应省内做唯一的阿拉伯语字形匹配，导出前校验省市组合。
- 收件区域没有来源，不会从街道猜测，也不会复制城市冒充区域。需按 GNT 的实际选项填写。
- 未标记付款的 cod 订单：COD amount 使用 order_total（包含运费、折扣等最终金额），不额外叠加运费。有付款日期的非 cod 订单设 0 并提示确认到账；其他情况留空待核对。
- 合并 line_item_N 的商品名和数量；不同订单不会合并。当前样例只有两笔单商品订单，多商品已用合成数据测试。
- 寄件资料由用户填写；重量、保险金额、Item type、Express product、FOD、RC 等没有可靠来源，保留空白让用户按 GNT 要求填写。币种目前仅支持 EGP。
- 输出保留模板的精确表头、列序、Sheet1 和 Sheet2 地区数据；不复制原文件的格式、宏或 Excel 数据验证规则。尚未在 GNT 实际导入验证。
- 不自动创建运单，不记录客户内容到服务器日志，不保存上传文件。订单数据刷新后清空；主动保存的寄件资料保留在当前浏览器中。

## 验证

```sh
.venv/bin/python -m unittest -v
```

固定寄件资料存放在本机 `sender-settings.json`，读取订单时自动应用，已被 Git 忽略。网页内可点击保存默认寄件资料，将其保存在当前浏览器；浏览器保存值优先于此文件。未保存的修改只影响当次操作。分享工具包前请注意其中是否包含这份商家资料。

真实订单文件不应提交到 Git；本仓库只包含公共模板结构，不含客户资料。
