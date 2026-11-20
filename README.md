# news-image-20261120-entry

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261120-blue)](https://make.fun/bounty/news-image-20261120)

Entry for the [make.fun](https://make.fun) competition
[news-image-20261120](https://make.fun/bounty/news-image-20261120):
**"Sum up 20 November's world news in one image"** ($250, top 50 share).

## The image

`entry.png` is a 1024x1024 broadsheet, **THE WORLD TODAY**, summing up
Friday 20 November 2026 in 26 real news stories:

- **Lead:** the first-ever Trump–Xi–Putin trilateral summit in Shenzhen
  (APEC sidelines, joint peace declaration).
- **World court:** the ICJ rules Myanmar committed genocide against the
  Rohingya (9-6), the first such finding against a state.
- **Markets:** Anthropic soars 17% on its Nasdaq debut; the S&P 500 falls
  2.02% for a fifth straight loss; Nikkei down 4.68%.
- Plus a world map with the six lead stories, a day-in-numbers box, 20 more
  stories, and a markets strip. Sources: BBC, Reuters, AP, Al Jazeera, ICJ,
  Nasdaq, IMD.

## The program

`main.py` (Python 3.13, standard library only, no network) writes the image
to `/output/entry.png`. It verifies the bundled image's SHA-256, then copies
the exact bytes. Two runs write byte-identical output.

```sh
python3 main.py
# wrote /output/entry.png (161772 bytes, sha256 78e47967...)
```

## License

MIT. See [LICENSE](LICENSE).
