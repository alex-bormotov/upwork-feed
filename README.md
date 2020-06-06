# UpWork feed

## Receive Your custom UpWork job feed in Telegram

![](https://github.com/alex-bormotov/upwork-feed/workflows/Github-CICD/badge.svg)   [![Codacy Badge](https://app.codacy.com/project/badge/Grade/f97d9c14ee174f6f878c7498e981dd0d)](https://www.codacy.com/manual/alex-bormotov/upwork-feed?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alex-bormotov/upwork-feed&amp;utm_campaign=Badge_Grade)

<details>
  <summary>Demo:</summary>

  ![](demo/upwork-feed-demo.gif)

</details>

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

> For using a country filter you need put the country name into array "filter_countries":

> Like so ["United States"] - that will be is equal to "send me jobs from the United States only"

> If you made such entry ["!India"] - that will be is equal to "send me jobs from any country, except India"

> Also, you can add more countries like so ["United States", "Canada"]

```bash
sudo chmod +x docker_ubuntu_install.sh && sudo ./docker_ubuntu_install.sh
```

```bash
sudo docker run -d --rm --mount src=`pwd`/config,target=/upwork-feed/config,type=bind skilfulll1/upwork-feed:latest
```
