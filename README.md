# OpenRR-5k

## 📄 **Paper**: https://arxiv.org/pdf/2604.10321

## 🏆 NTIRE 2026 SIRR Challenge Leaderboard

### Award Winners

| Prize | Team              | PSNR ↑ | SSIM ↑ | LPIPS ↓ | DISTS ↓ | NIQE ↓ | Subjective ↑ |
|------|------------------|--------|--------|---------|---------|--------|--------------|
| 🥇 1st | **RRay**          | **36.17** | 0.9758 | 0.0235 | 0.0135 | 3.7375 | **4.45** |
| 🥈 2nd | **Xreflect Master** | 36.05 | **0.9776** | **0.0210** | **0.0127** | 3.7648 | 4.31 |
| 🥈 2nd | **AIIALab**       | 35.38 | 0.9750 | 0.0231 | 0.0155 | 3.7737 | 4.23 |
| 🥉 3rd | **VIP Lab**       | 34.69 | 0.9766 | 0.0231 | 0.0148 | **3.7218** | 3.85 |
| 🥉 3rd | **YuFans**        | 34.91 | 0.9738 | 0.0257 | 0.0159 | 3.7783 | 3.59 |
| 🥉 3rd | **KLETech-CEVI**  | 34.54 | 0.9748 | 0.0242 | 0.0150 | 3.7566 | 3.57 |

> [!NOTE]
> PSNR, SSIM, LPIPS, DISTS, and NIQE are calculated on the **OpenRR-5k Validation set**, whereas Subjective scores are evaluated on the **OpenRR-5k Test set**; both sets of metrics represent results from the same model checkpoint.

### 📊 Full Leaderboard

| Rank | Team              | PSNR | SSIM | LPIPS | DISTS | NIQE | Subjective |
|------|------------------|------|------|-------|-------|------|------------|
| 1 | RRay | 36.1688 | 0.9758 | 0.0235 | 0.0135 | 3.7375 | 4.45 |
| 2 | Xreflect Master | 36.0496 | 0.9776 | 0.0210 | 0.0127 | 3.7648 | 4.31 |
| 3 | AIIALab | 35.3799 | 0.9750 | 0.0231 | 0.0155 | 3.7737 | 4.23 |
| 4 | VIP Lab | 34.6872 | 0.9766 | 0.0231 | 0.0148 | 3.7218 | 3.85 |
| 5 | YuFans | 34.9062 | 0.9738 | 0.0257 | 0.0159 | 3.7783 | 3.59 |
| 6 | KLETech-CEVI | 34.5375 | 0.9748 | 0.0242 | 0.0150 | 3.7566 | 3.57 |
| 7 | PSU | 34.5148 | 0.9746 | 0.0282 | 0.0191 | 3.7559 | 3.25 |
| 8 | SiGMoid | 34.2792 | 0.9749 | 0.0289 | 0.0205 | 3.7691 | 3.09 |
| 9 | NTR | 33.9679 | 0.9729 | 0.0323 | 0.0228 | 3.7639 | 3.01 |
| 10 | refineX | 30.5993 | 0.9715 | 0.0378 | 0.0291 | 3.7675 | 2.55 |
| - | OPPO Baseline | 31.62 | 0.9229 | 0.0566 | 0.0539 | 3.6205 | baseline |
| - | ACVLAB | 31.69 | 0.9241 | 0.0541 | 0.0551 | 3.6393 | late submission |


## Dataset

The OpenRR-5k dataset has been released on Hugging Face 🤗 [OpenRR-5k Dataset](https://huggingface.co/datasets/qiuzhangTiTi/OpenRR-5k), in conjunction with [NTIRE 2026](https://www.cvlai.net/ntire/2026/). Please visit the [CodaBench Competition](https://www.codabench.org/competitions/12971/) page for more details.

The dataset consists of the following components:
- `train_5000.zip`: contains paired input images and corresponding GT images;
- `val_300_blended.zip`: contains 300 validation input images only;
- `val_300_transmission.zip`: contains 300 validation GT only;
- `test_100_blended.zip`: contains input images only, without ground truth.

- `NTIRE2026_SIRR_TopTeam_Results.zip`: Visual Results for Top-6 Teams on Val and Test Sets.

## Citation

If you find our code helpful in your research or work please cite our paper.

```bibtex
@article{cai2026ntire,
  title={NTIRE 2026 Challenge on Single Image Reflection Removal in the Wild: Datasets, Results, and Methods},
  author={Cai, Jie and Yang, Kangning and Li, Zhiyuan and Vasluianu, Florin-Alexandru and Timofte, Radu and Li, Jinlong and Shen, Jinglin and Meng, Zibo and Cao, Junyan and Zhao, Lu and others},
  journal={arXiv preprint arXiv:2604.10321},
  year={2026}
}

@inproceedings{cai2025openrr,
  title={Openrr-5k: A large-scale benchmark for reflection removal in the wild},
  author={Cai, Jie and Yang, Kangning and Ouyang, Ling and Fu, Lan and Ding, Jiaming and Shen, Jinglin and Meng, Zibo},
  booktitle={2025 IEEE 8th International Conference on Multimedia Information Processing and Retrieval (MIPR)},
  pages={14--19},
  year={2025},
  organization={IEEE}
}
```
