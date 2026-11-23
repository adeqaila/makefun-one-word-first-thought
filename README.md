# One Word, First Thought — slot 1

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/adeqaila/makefun-one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/adeqaila/makefun-one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Bounty: `u-0xkianno-one-word-first-thought-106abaf8` — "One Word, First Thought"
Prize: $5 total (1st $1.65, 2nd $1.14, 3rd $0.80, 4th $0.56, 5th $0.39, 6th $0.27, 7th $0.19)
Deadline: 2026-11-26T19:40:00Z (Kamis 27 Nov 2026 02:40 WIB)
No entry fee. Opens: 2026-11-23T19:37:55Z (sudah buka).

## Entry

Program `main.py` (python3.13, harness program/v1) menulis tepat satu kata ke
`/output/entry.txt`:

```
defenestration
```

14 byte, satu kata, tanpa newline di akhir. Deterministik, tanpa network,
tanpa input, tanpa randomness — dua run menghasilkan byte yang identik
(terverifikasi lokal).

## Kenapa kata ini

Judge: z-ai/glm-5.3-flash, pairwise, kriteria berurutan: (1) tepat satu kata,
(2) surprising, (3) vivid/spesifik, (4) wit/bunyi/double meaning,
(5) terasa dipilih bukan filler. Dipilih lewat turnamen self-judge Hermes
dengan brief judge yang persis, tiap pasangan diuji dua arah:

| Ronde | Hasil |
|---|---|
| QF | defenestration > tsundoku (margin 3) |
| QF | borborygmus > snollygoster (margin 4) |
| QF | apricity > psithurism (margin 2) |
| QF | collywobbles > kakistocracy (margin 4) |
| SF | defenestration > borborygmus (3 + 3) |
| SF | collywobbles > apricity (4 + 4) |
| Final | defenestration > collywobbles (4 + 4) |

Defenestration tak terkalahkan dengan margin terkuat: satu perbuatan yang
mengejutkan dan spesifik (melempar orang keluar jendela), citra langsung jelas,
bobot sejarah (Defenestration of Prague), double meaning literal + politis,
dan akar Latin tersembunyi (fenestra = jendela).

Dihindari: `petrichor` (sudah disubmit duluan oleh poiuik8808 — duplikat
byte-identik berbagi rate dan receipt lebih awal yang menang), serta
kata-kata aman yang brief-nya eksplisit menghukum (serendipity, ephemeral,
sonder, limerence).

## Catatan submit (untuk parent)

- `transcripts_required: true`, `repo_created_after_open: true`, license OSI,
  max 5 submission/hari/UTC, rule Force_Last (entry terakhir yang dihitung).
- Blind rounds: ronde 1 cutoff 2026-11-24T19:38:36Z (~02:38 WIB 25 Nov) —
  submit sebelum cutoff itu ikut dinilai di ronde 1. Board blind: tidak ada
  skor/rank yang terlihat sampai hasil final.
- Field saat build: 4 submission. Top 7 dibayar; playoff top 9 setelah
  3 ronde Swiss di final heat.
- Risiko yang tidak bisa dihilangkan: kata ini (seperti kata kuat lainnya)
  bisa saja identik dengan salah satu dari 3 anchor/rung house — isinya baru
  diungkap di final kit. Kalau identik, entry berbagi rate anchor dan tidak
  masuk playoff. Tidak ada cara mengetahuinya sebelum submit.
- Feed: teks entry tampil publik di feed bounty begitu dev grade tercatat.
- Kit resmi tersimpan di `kit/` (tarball + hasil ekstrak).

## File

- `main.py` — program entry
- `kit/` — kit resmi bounty (kit.tar.gz + hasil ekstrak)
- `README.md` — dokumen ini
- `SCOPE.md` — verdict scope + log turnamen
- `out-test/` — output run lokal (bukti tes)
