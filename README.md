[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

# Tell a Whole Story in 32 Characters

Entry for the [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) bounty on [make.fun](https://make.fun).

## The entry

One Wi-Fi network name, 28 characters:

```
TherapyFailed_BoughtMeshWiFi
```

A couple went to therapy. It failed. So instead of fixing the marriage,
they bought mesh Wi-Fi — beginning, middle, and end in a name a stranger
reads in a phone's network list and gets on the first read.

## How it works

`main.py` (Python 3.13, standard library only) writes that exact string —
no trailing newline — to `/output/entry.txt`. It is fully deterministic:
two runs produce byte-identical output, and it uses no network.

```sh
python3 main.py
cat /output/entry.txt   # TherapyFailed_BoughtMeshWiFi
```

## License

MIT — see [LICENSE](LICENSE).
