import os
import urllib.request


cur_path = os.getcwd()
source_url_path = os.path.join(cur_path, 'raw_data')
image_dst_path = os.path.join(cur_path, 'img_data')

if not os.path.exists(image_dst_path):
	os.makedirs(image_dst_path)

total_files = 0  # 是否存放在一个大的文件夹下
for roots, parents, files in os.walk(source_url_path):
	for f in files:
		filename = os.path.join(roots, f)
		if total_files:
			prefix = filename.split('\\')[-3] + '__' + filename.split('\\')[-2] 
			img_list_queue = open(filename, "r").readlines()
			for img_list in img_list_queue:
				image = img_list.split('\n')[0]
				print("downloading and saving the image %s"%image)
				imagename = prefix + '__' + image.split('/')[-1]
				abs_imagename = os.path.join(image_dst_path, imagename)
				try:
					urllib.request.urlretrieve(image,filename=abs_imagename)
				except Exception:
					print("cannot download the image %s"%image)
		else:
			prefix = roots.split("raw_data\\")
			dst_abs_path = os.path.join(image_dst_path, prefix[1])
			
			if not os.path.exists(dst_abs_path):
				os.makedirs(dst_abs_path)
			img_list_queue = open(filename, "r").readlines()
			for img_list in img_list_queue:
				image = img_list.split('\n')[0]
				print("downloading and saving the image %s"%image)
				abs_imagename = os.path.join(dst_abs_path, image.split('/')[-1])
				
				
				try:
					urllib.request.urlretrieve(image,filename=abs_imagename)
				except Exception:
					print("cannot download the image %s"%image)
				