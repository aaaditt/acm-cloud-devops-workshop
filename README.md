# Cloud Quest

A five-level browser game about Day 1's concepts (IaaS/PaaS/SaaS, shared responsibility, AWS ↔ Azure ↔ Google Cloud, Dockerfiles, CI/CD). You play it inside a container you build yourself, so building and running it doubles as the Docker setup check. Nothing gets deployed: it only runs on your laptop.

Part of the ACM Cloud and DevOps Workshop (Day 1).

```bash
git clone https://github.com/aaaditt/cloud-quest.git
cd cloud-quest
docker build -t cloud-quest:v1 .
docker run -p 8080:8080 cloud-quest:v1
```

Open http://localhost:8080. The footer shows the container ID that is serving the game; compare it with `docker ps`.

Try a second container with different config from the same image:

```bash
docker run -p 8081:8080 -e VERSION=v2 cloud-quest:v1
```

No Docker yet? `pip install -r requirements.txt` then `python app.py` runs it directly.

| File | What it is |
| --- | --- |
| `app.py` | Flask app: serves the game and `/api/info` (container hostname + `VERSION`) |
| `static/index.html` | The whole game (no external dependencies, works offline) |
| `Dockerfile` | The same Dockerfile taught on Day 1 |
