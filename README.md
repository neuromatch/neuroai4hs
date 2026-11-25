# Neuro AI for High School

A course built with the [Neuromatch course kit](https://github.com/neuromatch/course-kit).
Pages are Markdown (MyST) in `tutorials/` and `projects/`; CI turns them into
the website, student and instructor notebooks, and solution files.

## Setup checklist

Do these once, after pushing this repository to GitHub.

- [ ] **Make the repository public.** Colab and Kaggle read the notebooks from raw GitHub URLs.
- [ ] **Turn on GitHub Pages.** Settings → Pages → **Source: GitHub Actions**. Add the custom domain there if you have one (no `CNAME` file needed).
- [ ] **Allow workflows to push.** Settings → Actions → General → Workflow permissions → **Read and write**. CI publishes the generated notebooks to the `notebooks-branch` branch, which it creates on the first run.
- [ ] **Push to `main`.** The `Course` workflow publishes the notebooks and the site.
- [ ] **Replace the example day** in `tutorials/` and the stub in `projects/` with your own, and update `project.toc` in `myst.yml`.
- [ ] **Optional: collect feedback.** Fill in the commented `nma.feedback` block in `myst.yml` with your own datatops project, then add `{nma-feedback}` to your pages.

## Working locally

```bash
uv venv && uv pip install neuromatch-course-kit -r requirements.txt
uv run nma-kit sync-assets     # the site's stylesheet and logos, once
uv run nma-kit check           # validate the content
uv run nma-kit notebooks       # generate notebooks into notebooks/
uv run myst start              # preview the site
```

`notebooks/`, `_build/` and `_nma/` are generated; they are git-ignored.

## Writing content

Tutorials live in `tutorials/W{week}D{day}_{Topic}/`: a `chapter_intro.md`,
`W{week}D{day}_Tutorial{n}.md` pages and a `further_reading.md`. See the
[course kit README](https://github.com/neuromatch/course-kit#readme) for the
directives (`{nma-video}`, `{nma-solution}`, `{nma-data}`, ...).
