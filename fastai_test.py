from duckduckgo_search import ddg_images
from fastdownload import download_url
from fastai.vision.all import *
import time

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

def search_and_download(term, destination, max_images = 1, show = False):
    print(f"Searching for '{term}'")
    urls = L(ddg_images(term, max_results = max_images)).itemgot('image')
    for i in range(len(urls)):
        try:
            file = '{:s}{:>03d}.jpg'.format(term, i)
            temp = (destination.parent / 'temp' / file)
            print(file)
            download_url(urls[i], temp, show_progress = False)
            if show:
                im = Image.open(temp)
                im.show()
            
            resize_image(file = file, dest = destination, src = temp.parent, max_size = 400)
        except:
            print("Failed to download image")

        #time.sleep(1)
    rm_tree(destination.parent / 'temp')

def main():
    searches = 'forest', 'bird'
    path = Path('forest_or_bird')
    num_images = 20
    train_size = 0.8
    epochs = 3
    test_image = 'bird.jpg'

    # download num_images per search
    for o in searches:
        search_and_download(o, (path/o), max_images = num_images)

    # instantiate a dataset
    dls = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=1-train_size, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(192, method='squish')]
    ).dataloaders(path, bs=32)

    # train the model
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(epochs)

    # do a prediction
    ret = learn.predict(PILImage.create(test_image))
    print(ret)
    result,_,probs = ret
    print(f"This is a: {result}.")
    print(f"Probability it's a bird: {probs[0]:.4f}")

if __name__ == '__main__':
    main()