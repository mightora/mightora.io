# Mightora tool directory

Edit `data/toolhub.yaml` to add new apps. All `groups` links go to the public tool site; `legacy` links are local docs. `content/_index.md` and `content/tools/_index.md` both render the same data with `tool-hub.html`. Keep `data/footer.yaml` and `static/footer.yaml` identical.

The original `update_cards.py` continues to regenerate the legacy Hugo documentation cards. The main homepage intentionally contains no `cards` shortcode, so it is not overwritten by that script.

Site pages are not offline applications. Each linked tool documents its own offline/privacy support. Validate with `python3 scripts/validate_toolhub.py`.

## Developer journey shortcuts

The four navigation panels (Build, Inspect, Architect, Deploy) appear above the six detailed tool categories. These are navigation shortcuts, not duplicates of the catalogue. The original tools are presented as **Power Platform toolkit** with equal prominence and complete documentation links. The author block is a compact, responsive variant of the official `mightora-author` component with an inline fallback, rather than the full-background hero style.
