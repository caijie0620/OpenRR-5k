import pyiqa
import os
import cv2
import glob
import torch
import numpy as np


def ls(filename):
    return sorted(glob.glob(filename))

class NTIRE_evaluation():
    def __init__(self):
        # self.psnr_range = [0,50]
        # self.ssim_range = [0.5,1]
        # self.lpips_range = [0,1]
        # self.dists_range = [0,1]
        # self.niqe_range = [0,1]

        # self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

        # self.iqa_psnr = pyiqa.create_metric('psnr', test_y_channel=True, color_space='ycbcr')
        # self.iqa_ssim = pyiqa.create_metric('ssim', test_y_channel=True, color_space='ycbcr')
        self.iqa_psnr = pyiqa.create_metric('psnr', test_y_channel=False)
        self.iqa_ssim = pyiqa.create_metric('ssim', test_y_channel=False)
        self.iqa_lpips = pyiqa.create_metric('lpips')
        self.iqa_dists = pyiqa.create_metric('dists')
        self.iqa_niqe = pyiqa.create_metric('niqe')

    def img2tensor(self, img, bgr2rgb, float32):
        '''
            Numpy array to tensor.

        Args:
            imgs (list[ndarray] | ndarray): Input images.
            bgr2rgb (bool): Whether to change bgr to rgb.
            float32 (bool): Whether to change to float32.
        '''
        if img.shape[2] == 3 and bgr2rgb:
            if img.dtype == 'float64':
                img = img.astype('float32')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = torch.from_numpy(img.transpose(2, 0, 1))
        if float32:
            img = img.float()
        return img
    
    def single_image_eval(self, in_path, ref_path):
        lr = cv2.imread(in_path, cv2.IMREAD_COLOR)
        lr = self.img2tensor(lr, bgr2rgb=True, float32=True).unsqueeze(0).contiguous()
        hr = cv2.imread(ref_path, cv2.IMREAD_COLOR)
        hr = self.img2tensor(hr, bgr2rgb=True, float32=True).unsqueeze(0).contiguous()
        if (lr.shape != hr.shape): raise ValueError("Bad prediction shape. Prediction shape: {}\nSolution shape:{}".format(lr.shape, hr.shape))

        hr = hr[..., 4:-4, 4:-4]/255.
        lr = lr[..., 4:-4, 4:-4]/255.

        PSNR = self.iqa_psnr(lr, hr).item()
        SSIM = self.iqa_ssim(lr, hr).item()
        LPIPS = self.iqa_lpips(lr, hr).item()
        DISTS = self.iqa_dists(lr, hr).item()
        NIQE = self.iqa_niqe(lr).item()
        
        return {'psnr':PSNR, 'ssim':SSIM, 'lpips':LPIPS, 'dists':DISTS, 'niqe':NIQE}


    def folder_score(self, lr_list, gt_list):
        psnr_list = []
        ssim_list = []
        lpips_list = []
        dists_list = []
        niqe_list = []

        for p in list(zip(lr_list, gt_list)):
            lr_path = p[0]
            hr_path = p[1]
            score_dict = self.single_image_eval(lr_path, hr_path)
            psnr_list.append(score_dict['psnr'])
            ssim_list.append(score_dict['ssim'])
            lpips_list.append(score_dict['lpips'])
            dists_list.append(score_dict['dists'])
            niqe_list.append(score_dict['niqe'])
        
        psnr_mean = np.array(psnr_list).mean()
        ssim_mean = np.array(ssim_list).mean()
        lpips_mean = np.array(lpips_list).mean()
        dists_mean = np.array(dists_list).mean()
        niqe_mean = np.array(niqe_list).mean()

        return psnr_mean, ssim_mean, lpips_mean, dists_mean, niqe_mean


# Default I/O directories:
default_result_dir = './OpenRR-5k_val/output'
default_GT_dir = './OpenRR-5k_val/transmission_layer'

output_dir =  "./"


if __name__ == '__main__':

    # Create the output directory, if it does not already exist and open output files
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    score_file = open(os.path.join(output_dir, 'scores.txt'), 'w')

    # Get all the solution files from the solution directory
    hr_list = sorted(ls(os.path.join(default_GT_dir, '*.jpg')))         # GT
    sr_list = sorted(ls(os.path.join(default_result_dir, '*.jpg')))     # model output 

    if (len(sr_list) != len(hr_list)): raise ValueError("Bad number of predictions. # of predictions: {}\n # of solutions:{}".format(len(sr_list), len(hr_list)))

    # Define the evaluation
    EvalScheme = NTIRE_evaluation()
    score = EvalScheme.folder_score(sr_list, hr_list)

    # Write score corresponding to selected task and metric to the output file
    score_file.write("PSNR: %0.4f\n" % float(score[0]))
    score_file.write("SSIM: %0.4f\n" % float(score[1]))
    score_file.write("LPIPS: %0.4f\n" % float(score[2]))
    score_file.write("DISTS: %0.4f\n" % float(score[3]))
    score_file.write("NIQE: %0.4f\n" % float(score[4]))
    # score_file.write("ExtraRuntime: %0.4f\n" % float(score))
    # score_file.write("ExtraPlatform: %0.4f\n" % float(score))
    # score_file.write("ExtraData: %0.4f\n" % float(score))

    score_file.close()

