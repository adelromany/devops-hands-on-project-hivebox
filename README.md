[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation

# Phase 1: Project Kickoff

## Objective

Build the project's foundation by setting up the GitHub repository, Git workflow, project structure, and project management tools.

---

## 1. Fork the Repository

Fork the original repository to your own GitHub account.

**Main Repository**

`https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox`

### Steps

1. Open the repository.
2. Click **Fork**.
3. Select your GitHub account.

### Why?

Forking creates your own copy of the repository under your GitHub account. This allows you to develop independently without affecting the original project while still being able to contribute through Pull Requests.

---

## 2. Clone Your Fork

Clone your fork to your local machine.

```bash
git clone https://github.com/YOUR-USERNAME/devops-hands-on-project-hivebox.git
cd devops-hands-on-project-hivebox
```

### Why?

Cloning downloads the repository to your computer so you can develop locally, commit changes, and synchronize them with your GitHub repository.

---

## 3. Configure the Upstream Remote

Add the original repository as an **upstream** remote.

```bash
git remote add upstream https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox.git
```

Verify the remotes:

```bash
git remote -v
```

Expected output:

* **origin** → Your fork (push your work here)
* **upstream** → Original project repository

### Why?

Because this project is based on a **fork**, your repository is a copy of the original project. The `upstream` remote allows you to pull future updates from the original repository and keep your fork synchronized while continuing to push your own work to `origin`.

---

## 4. Git Branching Strategy

Create the development branch.

```bash
git checkout -b development
```

Create the Phase 1 branch.

```bash
git checkout -b phase-1-kickoff
```

### Why?

Using separate branches keeps the project organized and prevents unfinished work from reaching the production branch.

* **main** contains stable, production-ready code.
* **development** integrates completed work before release.
* **phase-* branches** isolate work for each project phase, making development, testing, and code reviews easier.

> Never push directly to `main`. Every phase should be submitted through a Pull Request.

---

## 5. Create a GitHub Project Board

Create a Kanban board with the following columns:

* Backlog
* In Progress
* In Review
* Done

### Why?

A project board helps track progress, organize tasks, and visualize the project's workflow. It also makes collaboration easier by showing the current status of every task.

---

## 6. Create the Initial Project Structure

```bash
mkdir -p docs src tests

touch requirements.txt
touch src/__init__.py
touch docs/phase-1.md
```

### Why?

Organizing the project from the beginning improves maintainability.

* `src/` contains the application source code.
* `tests/` stores automated tests.
* `docs/` keeps project documentation.
* `requirements.txt` lists project dependencies.
* `README.md` explains how to use and contribute to the project.

---

## 7. Research the OpenSenseMap API

Test the API endpoints.

```bash
curl -s "https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786"
```

```bash
curl -s "https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786" | grep -i temperatur
```
The response should be something like this but with difference data

```bash
{"_id":"5eba5fbad46fb8001b799786","createdAt":"2022-03-30T11:25:43.857Z","updatedAt":"2026-07-10T13:09:47.587Z","name":"Groß Glienicke","currentLocation":{"type":"Point","coordinates":[13.110423,52.472952],"timestamp":"2023-05-23T13:29:38.495Z"},"grouptag":["bbumm"],"exposure":"outdoor","sensors":[{"title":"PM10","unit":"µg/m³","sensorType":"SDS 011","icon":"osem-cloud","_id":"5eba5fbad46fb8001b79978b","lastMeasurement":{"createdAt":"2026-07-10T13:09:47.578Z","value":"0.00"}},{"title":"PM2.5","unit":"µg/m³","sensorType":"SDS 011","icon":"osem-cloud","_id":"5eba5fbad46fb8001b79978a","lastMeasurement":{"createdAt":"2026-07-10T13:09:47.578Z","value":"0.00"}},{"title":"Temperatur","unit":"°C","sensorType":"BME280","icon":"osem-thermometer","_id":"5eba5fbad46fb8001b799789","lastMeasurement":{"createdAt":"2026-07-10T13:09:47.578Z","value":"26.06"}},{"title":"rel. Luftfeuchte","unit":"%","sensorType":"BME280","icon":"osem-humidity","_id":"5eba5fbad46fb8001b799788","lastMeasurement":{"createdAt":"2026-07-10T13:09:47.578Z","value":"55.67"}},{"title":"Luftdruck","unit":"Pa","sensorType":"BME280","icon":"osem-barometer","_id":"5eba5fbad46fb8001b799787","lastMeasurement":{"createdAt":"2026-07-10T13:09:47.578Z","value":"101337.72"}}],"model":"luftdaten_sds011_bme280","lastMeasurementAt":"2026-07-10T13:09:47.578Z","description":"ok-Lab Feinstaubsensor https://luftdaten.info/\nTerasse Straßenseite","image":"5eba5fbad46fb8001b799786_qa7mrg.jpg","loc":[{"geometry":{"type":"Point","coordinates":[13.110423,52.472952],"timestamp":"2023-05-23T13:29:38.495Z"},"type":"Feature"}]}
```

### Why?

Before writing code, it's important to understand the API you'll be integrating with. Inspecting the responses helps identify available endpoints, response formats, sensor names, and the data needed by the application.


---

## 8. Commit Your Work

```bash
git add .

git commit -m "docs: complete Phase 1 project setup and documentation"
```

Push your branch.

```bash
git push origin phase-1-kickoff
```

---

## 9. Create a Pull Request

Open a Pull Request from:

`phase-1-kickoff` → `main`

Merge it after review.



