import torch

def app():
    """
    A sample function that checks if CUDA is available.

    This function serves as an example template for checking
    the availability of CUDA-enabled GPUs in a PyTorch environment.
    
    Prints:
        A boolean value indicating whether CUDA is available.
    """
    print(torch.cuda.is_available())

    
if __name__ == '__main__':
    app()