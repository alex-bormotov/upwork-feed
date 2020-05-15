# UpWork feed

## Receive Your custom UpWork job feed in Telegram

![](https://github.com/alex-bormotov/upwork-feed/workflows/Github-CICD/badge.svg)   [![Codacy Badge](https://app.codacy.com/project/badge/Grade/f97d9c14ee174f6f878c7498e981dd0d)](https://www.codacy.com/manual/alex-bormotov/upwork-feed?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alex-bormotov/upwork-feed&amp;utm_campaign=Badge_Grade)

![](upwork-feed-demo.gif)

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
