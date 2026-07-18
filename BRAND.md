# Mightora — Brand & Design Guidelines for AI Agents

> **Purpose:** This document gives an AI coding agent everything it needs to build new Mightora websites and tools that match the established look, feel, and branding. Read it fully before generating any HTML, CSS, or copy for a Mightora project.

---

## 1. Brand Identity

| Property | Value |
|---|---|
| **Organisation** | Mightora (trading name of Tweed Technology Limited) |
| **Primary website** | https://mightora.io |
| **Created by** | Ian Tweedie, also known as TechTweedie |
| **Mission** | Provide free tools for the Microsoft Power Platform community |
| **Primary tagline** | *unleash the might of automation* |
| **Secondary tagline** | *with [N] free tools for the community* |

### Brand Family
There are three related brands that appear together in footers and headers. Always refer to them as a group when building site footers.

| Brand | URL | Description | Logo (raw) |
|---|---|---|---|
| **mightora.io** | https://mightora.io | Free tools for the Power Platform community | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/mightoraIoLogo4-200x900.png` |
| **Tech Tweedie** | https://techtweedie.github.io | Technical blog and tutorials by Ian Tweedie | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/TechTweedie_bw.png` |
| **Tweed.technology** | https://tweed.technology | Technology consulting by Ian Tweedie | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/tweedTechnologyLogoLight.png` |

---

## 2. Shared UI Library

All Mightora sites **must** load the shared UI library from the CDN before any site-specific styles or scripts. This provides pre-built Web Components and all design tokens.

```html
<!-- 1. Shared styles (load first) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/shared.css">

<!-- 2. js-yaml (required by the footer component) -->
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>

<!-- 3. Shared components -->
<script src="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/components.js" defer></script>
```

The library source lives at: https://github.com/mightora/shared-ui

---

## 3. Colour Palette

### Light Mode (default)
These are CSS custom properties defined on `:root` in `shared.css`.

| Token | Value | Use |
|---|---|---|
| `--primary` | `#111827` | Primary background, dark surface |
| `--primary-light` | `#059669` | Lighter primary variant |
| `--accent` | `#059669` | Emerald green — buttons, links, highlights |
| `--accent-hover` | `#047857` | Darker green on hover |
| `--success` | `#065f46` | Success states |
| `--success-light` | `#059669` | Light success / badge |
| `--warning` | `#e76f51` | Warning states |
| `--danger` | `#d62828` | Error / destructive actions |
| `--danger-light` | `#f07070` | Softer danger |
| `--info` | `#0096c7` | Informational highlights |
| `--text` | `#111827` | Primary body text |
| `--text-muted` | `#6b7280` | Secondary / supporting text |
| `--text-light` | `#9ca3af` | Placeholder, disabled text |
| `--bg` | `#f9fafb` | Page background |
| `--bg-card` | `#ffffff` | Card / panel background |
| `--bg-hover` | `#f3f4f6` | Hover state background |
| `--border` | `#e5e7eb` | Default border colour |
| `--border-focus` | `#059669` | Focus ring colour (matches accent) |

### Dark Mode
Applied via `[data-theme="dark"]` on `<html>`. Override only these tokens — everything else inherits from light mode.

| Token | Dark value |
|---|---|
| `--primary` | `#1f1f1f` |
| `--primary-light` | `#34d399` |
| `--accent` | `#34d399` |
| `--accent-hover` | `#6ee7b7` |
| `--success` | `#022c22` |
| `--success-light` | `#34d399` |
| `--text` | `#f3f4f6` |
| `--text-muted` | `#9ca3af` |
| `--text-light` | `#6b7280` |
| `--bg` | `#111827` |
| `--bg-card` | `#1f1f1f` |
| `--bg-hover` | `#2a2a2a` |
| `--border` | `#374151` |
| `--border-focus` | `#34d399` |

### mightora.io Site-Specific Override (Hugo / Hextra)
The main mightora.io site uses the Hextra Hugo theme with a custom green primary hue:

```css
:root {
  --primary-hue: 100deg;
  --primary-saturation: 90%;
}
```

Inline code colour on mightora.io: `#c97c2e` (amber/orange).

---

## 4. Typography

### Shared UI (non-Hugo sites)
- **Body font**: `system-ui, -apple-system, 'Segoe UI', sans-serif` (CSS variable `--font-sans`)
- **Monospace font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` (CSS variable `--font-mono`)
- **Base font size**: `16px`
- **Body line-height**: `1.6`
- **Paragraph line-height**: `1.7`

### Heading scale
| Element | Size |
|---|---|
| `h1` | `clamp(1.8rem, 4vw, 2.6rem)` |
| `h2` | `clamp(1.4rem, 3vw, 2rem)` |
| `h3` | `1.25rem` |
| `h4` | `1.1rem` |

All headings use `font-weight: 700` and `line-height: 1.3`.

### mightora.io Site-Specific (Hugo / Hextra)
- **Content font**: [Quicksand](https://fonts.google.com/specimen/Quicksand) — weights 300–700
- Load via: `@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');`
- Applied to `.content` elements only

---

## 5. Spacing, Layout & Border Radius

```css
/* Radii */
--radius-sm: 4px;
--radius:    8px;
--radius-lg: 12px;
--radius-xl: 16px;

/* Shadows */
--shadow-sm: 0 1px 3px rgba(0,0,0,.08);
--shadow:    0 4px 12px rgba(0,0,0,.10);
--shadow-lg: 0 8px 24px rgba(0,0,0,.12);

/* Header height */
--header-h: 60px;

/* Transition */
--transition: .2s ease;
```

### Container widths
```css
.container      { max-width: 1300px; margin: 0 auto; padding: 0 1.5rem; }
.container-wide { max-width: 1600px; margin: 0 auto; padding: 0 1.5rem; }
```

---

## 6. Logo & Favicon

### Navbar logo (mightora.io)
| Property | Value |
|---|---|
| Light mode logo | `/images/mightoraIoLogo4-200x900.png` |
| Dark mode logo | `/images/mightoraIoLogo4-200x900_invert.png` |
| Display width | `270px` |
| Display height | `60px` |
| Logo text | Hidden (logo image only, no site title text in nav) |

### Favicon / PWA metadata
```html
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="194x194" href="/favicon-194x194.png">
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#1c0835">
<meta name="apple-mobile-web-app-title" content="mightora.io">
<meta name="application-name" content="mightora.io">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="theme-color" content="#ffffff">
```

---

## 7. Component: Header (`<mightora-header>`)

Use the `<mightora-header>` Web Component. It handles sticky positioning, light/dark toggle, mobile menu, and logo display automatically.

```html
<mightora-header
  site-name="My Site"
  site-name-html="My <span>Site</span>"
  site-url="/"
  logo-light="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/main-logo.png"
  logo-dark="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/main-logo.png"
  theme-key="my-site-theme"
  nav-links='[
    {"label":"Home","url":"/"},
    {"label":"About","url":"/about"},
    {"label":"Tools ↗","url":"https://mightora.io/tools","ext":true}
  ]'>
</mightora-header>
```

### Header design rules
- Background: `#ffffff` (light) / `#1f1f1f` (dark)
- Border bottom: `1px solid #e5e7eb` (light) / `1px solid #2d2d2d` (dark)
- Height: `60px`, `position: sticky`, `top: 0`, `z-index: 100`
- Logo image max-height: `32px`, max-width: `160px`
- Logo is followed by a 1px vertical divider, then the site name text
- Site name text: `font-weight: 800`, `font-size: 1rem`, accent-coloured `<span>` for emphasis
- Nav links: `font-size: 0.875rem`, `font-weight: 500`, colour `#6b7280`, hover `#111827`
- External links in nav get the accent colour (`--accent`)
- Dark mode toggle and mobile hamburger button are always present

---

## 8. Component: Footer (`<mightora-footer>`)

Use the `<mightora-footer>` Web Component. It fetches navigation data from the shared YAML feed automatically.

```html
<mightora-footer
  yaml-url="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/footer.yaml">
  <!-- Site-specific copyright bar goes here as child HTML -->
  <div class="container">
    <div class="footer-bottom">
      <div class="footer-copy">
        &copy; <span class="footer-year"></span> My Site. All rights reserved.
      </div>
      <div class="footer-bottom-links">
        <a href="/privacy-policy/">Privacy</a>
        <a href="/terms/">Terms</a>
      </div>
    </div>
  </div>
</mightora-footer>
```

### Footer design rules
- Background: `#111827` (near-black, always dark regardless of page theme)
- Body text: `rgba(255,255,255,.75)`
- Layout: 3-column grid (`repeat(3, 1fr)`), collapses to 1 column on mobile (`max-width: 768px`)
- Section titles: `0.8rem`, `uppercase`, `letter-spacing: 0.1em`, `rgba(255,255,255,.5)`, `font-weight: 700`
- Links: `rgba(255,255,255,.65)`, `0.875rem`, hover: `#ffffff`
- **Brand logos strip** at the bottom: dark pill cards (`rgba(255,255,255,.06)` background, `1px solid rgba(255,255,255,.1)` border, `border-radius: 8px`)
  - Logo images: `height: 28px`, inverted to white with `filter: brightness(0) invert(1)` — **except** TechTweedie logo which uses `filter: none`
  - Brand description text: `0.75rem`, `rgba(255,255,255,.5)`
- Bottom bar: `border-top: 1px solid rgba(255,255,255,.1)`, copyright left, links right
- Copyright text: `0.8rem`, `rgba(255,255,255,.4)`

### Footer YAML feed
The shared footer data is at:
```
https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/footer.yaml
```
It defines three columns of navigation links and the three brand logo entries. Site-specific footers can point to a custom YAML file via the `yaml-url` attribute, or use the default shared feed to inherit all Mightora links.

---

## 9. Component: Author Section (`<mightora-author>`)

Used to display Ian Tweedie / TechTweedie as the creator. Fetches author data from a JSON config file.

```html
<mightora-author config-url="data/config.json"></mightora-author>
```

Expected `data/config.json` shape:
```json
{
  "author": {
    "name": "Ian Tweedie",
    "image": "https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/ian-tweedie-sq2.png",
    "bio": "Ian Tweedie (TechTweedie) is a Power Platform developer...",
    "branding": { "label": "TechTweedie" },
    "links": [
      { "label": "Blog", "url": "https://techtweedie.github.io", "icon": "fas fa-blog" },
      { "label": "GitHub", "url": "https://github.com/itweedie", "icon": "fab fa-github" }
    ]
  }
}
```

### Author section design rules
- Full-width section with `ian-tweedie-presenting-4.png` as a cover background image
  - CDN URL: `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/ian-tweedie-presenting-4.png`
- Dark overlay: `rgba(0,0,0,.45)`, padding `5rem 1.5rem`
- Max inner width: `780px`, centred, two-column layout (avatar + text)
- Avatar: `120px × 120px`, `border-radius: 50%`, white border `rgba(255,255,255,.4)`
- Blog logo displayed below avatar: `width: 110px`
- Heading: `1.375rem`, `font-weight: 800`, white
- Bio text: `0.9375rem`, `rgba(255,255,255,.88)`
- Link pills: `rgba(255,255,255,.15)` background, white text, `border: 1px solid rgba(255,255,255,.3)`

---

## 10. Tone of Voice & Copy

| Attribute | Guideline |
|---|---|
| **Audience** | Developers and citizen developers working with the Microsoft Power Platform |
| **Tone** | Friendly, practical, empowering — not corporate or stuffy |
| **Voice** | First person plural ("we", "our") — community-focused |
| **Taglines** | Bold and energetic: "unleash the might of automation" |
| **Free tools emphasis** | Always emphasise that tools are **free** and community-focused |
| **Technical level** | Assume the reader is a developer; use correct technical terminology |
| **CTAs** | Action-oriented: "Start building", "Explore our tools", "Get started" |

### Writing do's
- Highlight the free, open nature of all tools
- Reference the Power Platform community
- Use "empower" and "community" as value words
- Bold key benefits: `**Completely Free:**`, `**Boost Productivity:**`

### Writing don'ts
- Do not use aggressive marketing language
- Do not imply tools are paid or require sign-up
- Do not omit the legal note that Mightora is a trading name of Tweed Technology Limited in legal/about pages

---

## 11. Page Structure Pattern

A standard Mightora page follows this structure:

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title — mightora.io</title>

  <!-- Favicons (see Section 6) -->

  <!-- Shared UI -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/shared.css">
  <script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/components.js" defer></script>

  <!-- Site-specific styles -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Header -->
  <mightora-header
    site-name="Site Name"
    site-url="/"
    logo-light="..."
    nav-links='[...]'>
  </mightora-header>

  <!-- Main content -->
  <main class="container" style="padding: 2rem 1.5rem;">
    <!-- page content -->
  </main>

  <!-- Author section (optional) -->
  <mightora-author config-url="data/config.json"></mightora-author>

  <!-- Footer -->
  <mightora-footer>
    <div class="container">
      <div class="footer-bottom">
        <div class="footer-copy">&copy; <span class="footer-year"></span> mightora.io</div>
      </div>
    </div>
  </mightora-footer>

</body>
</html>
```

---

## 12. Hugo / Hextra Sites

When building sites on Hugo using the [Hextra theme](https://github.com/imfing/hextra), use these additional conventions:

- Theme module path: `github.com/imfing/hextra`
- Primary colour override in `custom.css`:
  ```css
  :root {
    --primary-hue: 100deg;
    --primary-saturation: 90%;
  }
  ```
- Navbar: logo only (`displayTitle: false`, `displayLogo: true`), logo width `270`, height `60`
- Footer: `displayCopyright: false`, `displayPoweredBy: false` — use the custom footer partial instead
- Footer partial reads from `data/footer.yaml`; brands appear as white-background pill cards (`.footer-brand-pill`)
- Content font: Quicksand (see Section 4)
- Allow raw HTML in Markdown: `goldmark.renderer.unsafe: true`
- Syntax highlighting: `highlight.noClasses: false`

---

## 13. Key Asset URLs

| Asset | URL |
|---|---|
| Shared CSS | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/shared.css` |
| Shared JS components | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/components.js` |
| Footer YAML feed | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/footer.yaml` |
| mightora.io logo (light) | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/mightoraIoLogo4-200x900.png` |
| mightora.io logo (dark/inverted) | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/mightoraIoLogo4-200x900_invert.png` |
| TechTweedie logo | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/TechTweedie_bw.png` |
| Tweed.technology logo | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/tweedTechnologyLogoLight.png` |
| Mightora swirl mark | `https://raw.githubusercontent.com/mightora/mightora.io/main/static/images/mightora-io-swirl.png` |
| Author avatar (Ian Tweedie) | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/ian-tweedie-sq2.png` |
| Author background photo | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/ian-tweedie-presenting-4.png` |
| TechTweedie blog logo | `https://cdn.jsdelivr.net/gh/mightora/shared-ui@main/main-logo.png` |

---

## 14. Social & Community Links

These links should be used consistently across all sites and footers:

| Platform | URL |
|---|---|
| GitHub (org) | https://github.com/mightora |
| GitHub (personal) | https://github.com/itweedie |
| YouTube | https://youtube.com/@techtweedie |
| Medium | https://medium.com/@ian.tweedie |
| LinkedIn | https://go.iantweedie.biz/LinkedIn-Linktree |
| Twitter/X | https://twitter.com/itweedie |
| Sessionize | https://sessionize.com/ian-tweedie/ |
| All links | https://linktr.ee/itweedie |
| Contact | https://iantweedie.biz |
| Coaching | https://partners.simply.coach/ian-tweedie |
| Status page | https://stats.uptimerobot.com/3EPW8gBu4N |
| Power Platform Clinic | https://powerplatformclinic.github.io |

---

## 15. How to Use This Document

**For AI agents building a new Mightora site:**
1. Load `shared.css` and `components.js` from the CDN (Section 2)
2. Use `<mightora-header>` and `<mightora-footer>` components (Sections 7–8)
3. Apply design tokens from Section 3 for any custom styles — never hardcode colour hex values when a token exists
4. Follow the page structure template in Section 11
5. Use the tone guidelines in Section 10 for all copy
6. Pull logos and assets from the URLs in Section 13 — do not re-host them

**For AI agents updating an existing site:**
- Do not change the accent colour away from `#059669` (light) / `#34d399` (dark)
- Do not replace the shared footer component with a custom footer — maintain the brand family links
- Do not change the footer background away from `#111827`
