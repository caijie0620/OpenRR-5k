# OpenRR-5k

## Please refer to the following link for the final LaTeX FactSheet submission.

[LaTex Submission Guidelines](https://github.com/caijie0620/OpenRR-5k/issues/8)


## Model Requirements & Evaluation Criteria
- Model Checkpoint Requirement: It is mandatory to use the same model checkpoint for both Val and Test.
- PSNR Threshold: We will set a PSNR threshold of 32 as the baseline. Additionally, the current highest submission on Val is over 36.
- Evaluation Eligibility: Models with a PSNR above the 32 threshold will be eligible for the final human evaluation on the test set. For models with a PSNR score below 32 dB, please refer to the details in [Github Issue](https://github.com/caijie0620/OpenRR-5k/issues/6) for the supplementary submission requirements.
- Why: We would prefer participants to focus on optimizing their models' performance on the test set, rather than devoting excessive effort to maximizing the PSNR score on the validation set.


## Submission Guidelines

Please send the following three required items to both caijie0620@gmail.com and zhiyuanli1992@gmail.com before March 17, 23:59 PM PT.
- val_300_output.zip: Contains only 300 validation output images.
- test_100_output.zip: Contains only 100 test output images.
- Links to or a zip file of the inference code.
- Email Subject: TeamName
- Email Content: CodeBench username, Team Leader Name/Email/Affiliation, as well as the CodeBench PSNR/SSIM/LPIPS scores for the final model, Training Data, and optional explanation if your Val PSNR < 32.

Note: The Methods LaTeX FactSheet is not required; only top teams will be asked to submit it after March 17.


## Dataset

The OpenRR-5k dataset has been released on Hugging Face 🤗 [OpenRR-5k Dataset](https://huggingface.co/datasets/qiuzhangTiTi/OpenRR-5k), in conjunction with [NTIRE 2026](https://www.cvlai.net/ntire/2026/). Please visit the [CodaBench Competition](https://www.codabench.org/competitions/12971/) page for more details.

The dataset consists of the following components:
- `train_5000.zip`: contains paired input images and corresponding GT images;
- `val_300_blended.zip`: contains 300 validation input images only;
- `val_300_transmission.zip`: contains 300 validation GT only;
- `test_100_blended.zip`: contains input images only, without ground truth.


## Citation

If you find our code helpful in your research or work please cite our paper.

```bibtex
@inproceedings{cai2025openrr,
  title={Openrr-5k: A large-scale benchmark for reflection removal in the wild},
  author={Cai, Jie and Yang, Kangning and Ouyang, Ling and Fu, Lan and Ding, Jiaming and Shen, Jinglin and Meng, Zibo},
  booktitle={2025 IEEE 8th International Conference on Multimedia Information Processing and Retrieval (MIPR)},
  pages={14--19},
  year={2025},
  organization={IEEE}
}
```
