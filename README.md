# Finance portfolio template

A responsive HTML and CSS portfolio in navy, blue, grey and white. No build tools or runtime dependencies are required. A small vanilla JavaScript file supports theme switching and the illustrative market ticker. Includes expertise, expandable sample case studies, experience, PDF downloads and a Netlify contact form.

## Customise

- Edit `index.html` for your name, introduction, projects, career history, qualifications, email and social links. The current experience and education are drawn from the supplied CV; review them for accuracy before publishing.
- Replace the two root-level PDF files with your own documents, keeping filenames or updating every download link. Anything published in this repository is publicly downloadable.
- Change the palette and fonts in the `:root` variables in `styles.css`. Google Fonts are optional; system fonts work offline.
- Edit `thanks.html` for the contact confirmation message and `favicon.svg` for the site icon.

## Run locally

From this directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open port 8000 locally. The local server displays the site but does not process form submissions.

## Deploy from GitHub to Netlify

1. Commit these files and push them to your GitHub repository.
2. In Netlify, add a project by importing an existing Git repository, choose GitHub, and select this repository.
3. Choose the `main` production branch. Leave the build command empty and use `.` as the publish directory (also set in `netlify.toml`). Deploy the site.
4. Enable Netlify form detection in your project settings if it is not already enabled, then redeploy. Confirm that the `contact` form appears in Netlify's Forms area.
5. Submit a real test message on the deployed site, check the confirmation page and verify receipt in Forms. Set up email notifications in Netlify if desired.

Future pushes to the connected production branch trigger automatic deployments. No secrets or environment variables are required for this template. Netlify's service limits and spam filtering apply to form submissions.

## Market ticker, themes and PDFs

The dark market bar shows **illustrative, static quotes, not live prices**. It covers selected major equity indices and USD, EUR, GBP, JPY, CHF, CAD, AUD and NZD against MYR (MYR per one unit of foreign currency). Values and percentage changes are fictional examples, not a market snapshot. Edit `quotes` in `app.js`. Production live quotes require a licensed data source and secure server-side integration; do not put API keys in browser code. Pause the animation with the button; reduced-motion settings disable scrolling.

Light/dark mode follows the device initially and remembers explicit choices locally when storage is available. The entire site, including the confirmation page, supports both palettes.

Visitors can download the A4 interview CV and six-slide 16:9 profile deck without browser printing. Both are static PDFs. To regenerate them after updating the content, install ReportLab in a development environment and run `python3 tools/generate_pdfs.py`. PDF generation is not needed for Netlify deployment. The website headline describes the desired profile; the CV preserves the actual FSTEP employment title.
