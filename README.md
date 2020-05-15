![](https://github.com/alex-bormotov/upwork-feed/workflows/Github-CICD/badge.svg)

![Codacy Badge](https://www.codacy.com/manual/alex-bormotov/upwork-feed?utm_source=github.com&utm_medium=referral&utm_content=alex-bormotov/upwork-feed&utm_campaign=Badge_Grade_Dashboard)

# upwork-feed

## Receive Your custom UpWork job feed in Telegram

### Install (Ubuntu + Docker)

```bash
git clone https://github.com/alex-bormotov/upwork-feed
```

```bash
cd upwork-feed
```

```bash
cp config/config.json.sample config/config.json
```

> Edit config/config.json

```bash
sudo chmod +x docker_ubuntu_install.sh && sudo ./docker_ubuntu_install.sh
```

```bash
sudo docker run -d --rm --mount src=`pwd`/config,target=/upwork-feed/config,type=bind skilfulll1/upwork-feed:latest
```
