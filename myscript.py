import numpy as np
import hydra
import time

@hydra.main(config_path='conf', config_name="conf")
def main(cfg):
    print("Hello from myscript with param {}".format(cfg.myparam))
    np.savetxt('param_{}.txt'.format(cfg.myparam),
        np.array([42]))

if __name__ == "__main__":
    main()