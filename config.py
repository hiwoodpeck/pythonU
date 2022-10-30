# coding,utf-8
common_ports = [
    [21, "FTP服务所开放的端口，用于上传、下载文件。"],
    [22, "SSH端口，用于通过命令行模式远程连接Linux服务器或vps。"],
    [23, "Telnet端口，用于Telnet远程登录服务器。"],
    [25, "SMTP服务所开放的端口，用于发送邮件。"],
    [80, "HTTP用于HTTP服务提供访问功能，例如，IIS、Apache、Nginx 等服务。"],
    [110, "POP3用于POP3 协议，POP3 是电子邮件收发的协议。"],
    [143, "IMAP用于IMAP（Internet Message Access Protocol）协议，IMAP 是用于电子邮件的接收的协议。"],
    [443, "HTTPS 用于HTTPS服务提供访问功能。HTTPS 是一种能提供加密和通过安全端口传输的一种协议。"],
    [1433, "SQL Server SQL Server的TCP 端口，用于供SQL Server对外提供服务。"],
    [1434, "SQL Server SQL Server的UDP端口，用于返回SQL Server使用了哪个 TCP/IP 端口。"],
    [1521, "Oracle通信端口，服务器上部署了Oracle SQL需要放行的端口。"],
    [3306, "MySQL数据库对外提供服务的端口。"],
    [3389, "远程桌面服务端口，可以通过这个端口远程连接服务器。"],
    [8080, "代理端口,同80端口一样，8080 端口常用于WWW代理服务，实现网页浏览。"],
]
