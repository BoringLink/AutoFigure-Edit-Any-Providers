# Citation And Attribution

<<<<<<< HEAD
This page explains how we hope people cite and acknowledge AutoFigure.
=======
This page explains how we hope people cite and acknowledge AutoFigure-Edit.
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)

This document is intentionally gentle:

- it is a request for fair academic attribution
- it is not an extra restriction added to the software license
- it is not legal advice

## Short version

<<<<<<< HEAD
If AutoFigure materially helps a paper, report, benchmark write-up, demo, or public figure artifact, please:

1. cite the AutoFigure paper
2. disclose meaningful AI assistance honestly
3. avoid presenting AI-generated figures as fully manual if that would mislead readers

If you only used AutoFigure in a minor operational way, such as launching a local script, browsing files, or testing a setup, citation is usually not necessary.

## When we strongly encourage citation

Citation is strongly encouraged when AutoFigure materially contributes to work such as:

- generating publication figures from text descriptions
- extracting methodology from papers and producing draft figures
- iterative figure refinement or evaluation that meaningfully shapes a public artifact
- benchmarks, demos, or case studies that materially depend on AutoFigure outputs

The practical rule is simple:

- if AutoFigure changed the substance, speed, or shape of the published figure or research artifact in a meaningful way, please cite it

## When citation is usually not necessary

Citation is usually unnecessary when AutoFigure was used only as:

- a local launcher
- a terminal convenience layer
- a setup helper without material figure or research contribution
- a one-off operational utility
=======
If AutoFigure-Edit materially helps a paper, report, benchmark write-up, demo, or public figure artifact, please:

1. cite the AutoFigure-Edit paper
2. disclose meaningful AI assistance honestly
3. avoid presenting AI-generated or AI-edited figures as fully manual if that would mislead readers

If you only used AutoFigure-Edit in a minor operational way, such as launching the server, checking the repository layout, or testing a local setup, citation is usually not necessary.

## When we strongly encourage citation

Citation is strongly encouraged when AutoFigure-Edit materially contributes to work such as:

- turning method text into editable SVG figures
- drafting or refining figures that appear in a paper, report, blog post, poster, or slide deck
- AI-assisted figure editing, assembly, or iterative visual revision
- public demos, case studies, or benchmarks that materially depend on AutoFigure-Edit outputs

The practical rule is simple:

- if AutoFigure-Edit changed the substance, speed, or shape of the published figure or research artifact in a meaningful way, please cite it

## When citation is usually not necessary

Citation is usually unnecessary when AutoFigure-Edit was used only as:

- a local launcher
- a setup or deployment convenience
- a one-off operational helper without material contribution to the figure or research output
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)

## Preferred citation

Paper link:

<<<<<<< HEAD
- `https://openreview.net/forum?id=5N3z9JQJKq`
=======
- `https://arxiv.org/abs/2603.06674`
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)

BibTeX:

```bibtex
<<<<<<< HEAD
@inproceedings{
zhu2026autofigure,
title={AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations},
author={Minjun Zhu and Zhen Lin and Yixuan Weng and Panzhong Lu and Qiujie Xie and Yifan Wei and Sifan Liu and Qiyao Sun and Yue Zhang},
booktitle={The Fourteenth International Conference on Learning Representations},
year={2026},
url={https://openreview.net/forum?id=5N3z9JQJKq}
=======
@misc{lin2026autofigureeditgeneratingeditablescientific,
  title={AutoFigure-Edit: Generating Editable Scientific Illustration},
  author={Zhen Lin and Qiujie Xie and Minjun Zhu and Shichen Li and Qiyao Sun and Enhao Gu and Yiran Ding and Ke Sun and Fang Guo and Panzhong Lu and Zhiyuan Ning and Yixuan Weng and Yue Zhang},
  year={2026},
  eprint={2603.06674},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2603.06674}
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)
}
```

## Suggested acknowledgment text

<<<<<<< HEAD
If AutoFigure materially assisted the project, a short acknowledgment like the following is usually enough:

```text
We used AutoFigure to assist parts of the figure-generation workflow, including selected drafting, refinement, and/or evaluation of scientific illustrations. Final scientific claims, reported results, and publication decisions remain the responsibility of the human authors.
=======
If AutoFigure-Edit materially assisted the project, a short acknowledgment like the following is usually enough:

```text
We used AutoFigure-Edit to assist parts of the figure-generation and figure-editing workflow, including selected SVG drafting, structured refinement, and/or assembly of scientific illustrations. Final scientific claims, reported results, and publication decisions remain the responsibility of the human authors.
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)
```

You can shorten or adapt this wording to match venue norms.

## AI assistance disclosure

<<<<<<< HEAD
We strongly encourage clear disclosure when AutoFigure contributed to:

- figure generation
- figure drafting or refinement
- prompt design for published visuals
- benchmark or demo outputs that showcase generated figures
=======
We strongly encourage clear disclosure when AutoFigure-Edit contributed to:

- figure generation
- SVG drafting or reconstruction
- figure editing or assembly
- prompt iteration for published visuals
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)

The disclosure does not need to overstate use.
It should simply help readers understand where meaningful AI assistance existed.

<<<<<<< HEAD
## FigureBench note

If your public benchmark or dataset usage materially depends on FigureBench, we also encourage citing the FigureBench dataset record used in your work when applicable.

=======
>>>>>>> d0e7f23 (docs: simplify citation attribution doc path)
## Not a license condition

This citation guidance does not change the repository software license.

In particular:

- it is not a new license condition
- it does not terminate your software rights if you forget to cite
- it is a community and academic attribution request, not a software-usage gate

## Related files

- [CITATION.cff](./CITATION.cff)
- [TRADEMARK.md](./TRADEMARK.md)
- [README.md](./README.md)
