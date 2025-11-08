# GitHub CLI setup (gh)

These commands create both the **public** and **private** repositories directly from your local folders.

---

## 🧭 1️⃣ One-time setup
Authenticate GitHub CLI:
```bash
gh auth login
```
Select **GitHub.com**, **HTTPS**, and **Authenticate with browser** (only once).

---

## 🟩 2️⃣ Public repository
```bash
cd ~/Proyectos
unzip ~/Descargas/gobekli-finder-public.zip -d gobekli-finder
cd gobekli-finder
git init
git add .
git commit -m "init: public repo with pipeline and docs"

gh repo create dsilberschmidt/gobekli-finder \
  --public \
  --source=. \
  --remote=origin \
  --push
```

Verify:
```bash
gh repo view --web
```

---

## 🔒 3️⃣ Private repository
```bash
cd ~/Proyectos
unzip ~/Descargas/gobekli-finder-private.zip -d gobekli-finder-private
cd gobekli-finder-private
git init
git add .
git commit -m "init: private repo with data structure and workflow"

gh repo create dsilberschmidt/gobekli-finder-private \
  --private \
  --source=. \
  --remote=origin \
  --push
```

Verify:
```bash
gh repo view --web
```

---

## ⚙️ 4️⃣ Update after changes
```bash
git add .
git commit -m "update: description"
git push
```
