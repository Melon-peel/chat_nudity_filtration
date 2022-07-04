import os
from nsfw_detector import predict
from tqdm import tqdm
import json
import shutil
import argparse

class NudesClassifier():

    '''
    NSFW classifier of pictures

    Parameters
    ------------------
    vars_path: str
        Path to the file containing the values of the parameters listed below. Current directory by default

    is_recursive : int
        Whether to look for pictures to be classified in all the subdirectories of `picturess_dir` (1 if yes). 0 by default
    track_progress: int
        Whether to display progress bar of classification in console (1 if yes). 1 by default
    model_path: str
        Path to the model. Keras 299x299 in the current directory by default
    image_dim: int
        Dim parameter for the model. 299 by default, a the default model is 299x299
    pictures_dir: str
        Path to the directory with pictures to be classified. Current directory by default
    output_dir: str        
        Path to the directory where a folder with results will be created. Current directory by default
    hentai_param: float
        Hyperparameter, see GitHub repo for more @chat_nudity_filtration
    porn_param: float
        Hyperparameter, see GitHub repo for more @chat_nudity_filtration
    '''



    def __init__(self, vars_path=os.path.join(os.getcwd(), 'vars.json')):
        self.class_names = ("SFW", "NSFW", "Sexy")
        self.is_recursive = None
        self.track_progress = None
        self.model_path = None
        self.image_dim = None
        self.pictures_dir = None
        self.output_dir = None
        self.hentai_param = None
        self.porn_param = None
        self.vars_path = vars_path


        self.generator_pics = None
        self.pictures_paths = None
        self.dest_paths = dict()

        self.model = None
        self.set_vars()


    def get_generator_recursive(self, gen_):
        for i in gen_:
            for j in i:
                yield j

    def set_vars(self):
        with open(self.vars_path, "r") as f:
            vars_classifier = json.load(f)
        for attr_name in vars_classifier:
            self.__setattr__(attr_name, vars_classifier[attr_name])
        if not self.pictures_dir:
            self.pictures_dir = os.getcwd()
        if not self.model_path:
            self.model_path = os.path.join(os.getcwd(), "nsfw.299x299.h5")
        
        
        # create dirs
        if not self.output_dir:
            base_output_path = os.path.join(self.pictures_dir, "NSFWs_classified")
            if not os.path.exists(base_output_path):
                os.mkdir(base_output_path)
            self.output_dir = base_output_path
                        
        classified_dirs = [os.path.join(self.output_dir, class_name) for class_name in self.class_names]
        for i, classified_dir in enumerate(classified_dirs):
            if not os.path.exists(classified_dir):
                os.mkdir(os.path.join(self.output_dir, self.class_names[i]))
            

        self.dest_paths.update({"SFW": os.path.join(self.output_dir, "SFW"),
                                "NSFW": os.path.join(self.output_dir, "NSFW"),
                                "Sexy": os.path.join(self.output_dir, "Sexy")})
        # -------
        # get list of img files

        if self.is_recursive:            
            dir_files = os.walk(self.pictures_dir)  # generator
            gen_ = ([os.path.join(root, i) for i in files if i.split(".")[-1] in {"jpg", "png", "jpeg"}] for root, _, files in os.walk(self.pictures_dir) if root.find(self.output_dir) == -1)
            self.pictures_paths = self.get_generator_recursive(gen_)  # generator yeilding paths of pictures
        else:
            dir_files = os.listdir(self.pictures_dir)  # list
            self.pictures_paths = (os.path.join(self.pictures_dir, file_name)  for file_name in dir_files if file_name.split(".")[-1] in {"jpg", "jpeg", "png"})
    

    def initalize_model(self):
        self.model = predict.load_model(self.model_path)


    def run_body(self, image_path):
        pic_cats = predict.classify(self.model, image_path, image_dim=self.image_dim)[image_path]

        hentai_p = pic_cats['hentai']
        porn_p = pic_cats['porn']
        sexy_p = pic_cats['sexy']


        if hentai_p > self.hentai_param:  
            shutil.copy2(image_path, self.dest_paths['NSFW'])
        elif (porn_p > self.porn_param) and (self.sexy_param_upper > sexy_p):
            shutil.copy2(image_path, self.dest_paths['NSFW'])
        elif sexy_p > self.sexy_param_upper:
            shutil.copy2(image_path, self.dest_paths['Sexy'])
        else:
            shutil.copy2(image_path, self.dest_paths['SFW'])        


    def classify(self):    
        if self.track_progress:
            for image_path in tqdm(list(self.pictures_paths)):
                self.run_body(image_path)
        else:
            for image_path in self.pictures_paths:
                self.run_body(image_path)
    def run(self):
        self.initalize_model()
        self.classify()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--vars')

    args = parser.parse_args()

    if args.vars:
        classifier = NudesClassifier(args.vars)
    else:
        classifier = NudesClassifier()

    classifier.run()