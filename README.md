# Student Survey WS25/26

A multi-wave student survey built with [oTree](https://www.otree.org/) (v6.0.4), designed for collecting data on political attitudes, social networks, migration opinions, AI usage, and academic motivation among university students.

## Project Overview

The survey consists of 9 sequential apps covering the following topics:

| App | Topic | Description |
|-----|-------|-------------|
| `app_start` | Welcome | Device info collection, language selection |
| `app_demographic` | Demographics | Age, gender, family education background (3 generations), financial situation |
| `app_vignette` | Military Service Experiment | Randomized vignette on Wehrdienst (108 treatment combinations) |
| `app_network` | Social Networks | Ego-network module with up to 50 alters, relationship attributes, political positioning |
| `app_migration` | Migration Attitudes | Economic and cultural dimensions of immigration policy |
| `app_AI` | AI Usage | AI tool adoption in academic context (ChatGPT, Claude, Gemini, etc.) |
| `app_political` | Political Attitudes | Party preference, scalometer, social media usage, participation |
| `app_studium` | Academic Motivation | Study strategies, class engagement, MSL scale items |
| `app_end` | Completion | Verification codes, feedback, confirmation |

## Tech Stack

- **Framework:** oTree 6.0.4 (Python)
- **Runtime:** Python 3.12
- **Database:** PostgreSQL 16 (production) / SQLite (local dev)
- **Containerization:** Docker + Docker Compose
- **Error Tracking:** Sentry SDK

## Local Development

### Prerequisites

- Python 3.12+
- pip

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
otree devserver
```

The server starts at `http://localhost:8000`. The admin interface is available at `http://localhost:8000/admin`.

### Demo

Navigate to `http://localhost:8000/demo` to access the demo session with 3 participants.

## Docker Deployment (Production)

### Prerequisites

- Docker & Docker Compose

### Environment Files

The project uses two env files:

- **`config.env`** (committed) — contains non-sensitive config like `OTREE_AUTH_LEVEL`, `POSTGRES_USER`, `POSTGRES_DB`
- **`secrets.env`** (git-ignored) — you must create this file with:

```env
POSTGRES_PASSWORD=<your-db-password>
OTREE_ADMIN_PASSWORD=<your-admin-password>
OTREE_REST_KEY=<your-rest-api-key>
```

### Build & Run

```bash
# Build and start containers (detached)
docker compose up -d --build

# View running containers
docker ps

# View logs
docker logs <container-name>

# Shell into the oTree container
docker exec -ti <container-name> sh

# Stop and remove everything (containers, images, volumes)
docker compose down --rmi all -v
```

### Architecture

```
┌──────────────┐      ┌──────────────────┐
│   Browser    │─────▶│  oTree (py3.12)  │
│  Port 8000   │      │  Alpine Linux    │
└──────────────┘      └───────┬──────────┘
                              │
                      ┌───────▼──────────┐
                      │  PostgreSQL 16   │
                      │  Port 5432       │
                      │  Persistent Vol  │
                      └──────────────────┘
```

Both services auto-restart and have log rotation (1MB max, 3 files).

### Remote Server Deployment

To deploy on a remote server via SSH:

```bash
# Create a Docker context for the remote server
docker context create --docker 'host=ssh://ubuntu@<server-address>' <context-name>

# Switch to remote context
docker context use <context-name>

# Now all docker commands run on the remote server
docker compose up -d --build
```

## oTree Administration

### Session & Room Config

The survey is configured as a single session (`SS_WS2526`) with a room called `MethodsLecture`:

- **Auth Level:** `STUDY` — participants need a valid link to access the survey
- **Participant Codes:** defined in `_rooms/code_list.txt`

### Creating a Session

1. Go to `http://<host>:8000/admin`
2. Log in with admin credentials
3. Click **Rooms** → **MethodsLecture** → create a session
4. Distribute participant links to students

### Data Export

1. Admin panel → **Data** → **Export**
2. Download per-app CSV or the wide-format combined export

### Resetting the Database

```bash
# Local
otree resetdb

# Docker
docker exec -ti <container-name> otree resetdb
```

## Project Structure

```
├── settings.py              # oTree configuration
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container image definition
├── compose.yaml             # Docker Compose services
├── config.env               # Non-sensitive environment config
├── secrets.env              # Sensitive credentials (git-ignored)
├── _rooms/                  # Room config & participant codes
├── _static/                 # CSS, JS, images
├── _templates/              # Base HTML templates
├── app_*/                   # Survey apps (models, pages, templates, questions.json)
├── utils/                   # Bot testing, code creation, participant tracking
└── documentation/           # Codebook, internal docs
```

Each app follows the standard oTree structure:

```
app_<name>/
├── models.py          # Data fields and player model
├── pages.py           # Page sequence and form logic
├── constants.py       # App-level constants
├── questions.json     # Question texts (supports i18n)
└── templates/         # HTML templates
```

## License

This project is intended for academic research use.
