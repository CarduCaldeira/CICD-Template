import torch

def test_pytorch_cuda():
    """
    A sample template to test CUDA functionality with PyTorch.

    This function checks if CUDA is available and then performs
    operations on tensors to ensure that computation can be 
    correctly moved between CPU and a CUDA-enabled GPU.

    Raises:
        AssertionError: If CUDA is not available or if the tensor 
        results on CPU and GPU do not match.

    Prints:
        A message confirming CUDA availability and the name of the GPU used.
        Details of tensor operations performed on both the CPU and GPU.
    """

    assert torch.cuda.is_available(), "CUDA não está disponível no ambiente."

    device = torch.device('cuda')
    device_name = torch.cuda.get_device_name(device)
    print(f"CUDA está disponível. Usando GPU: {device_name}")

    tensor_cpu = torch.rand(3, 3)
    print("Tensor criado no CPU:\n", tensor_cpu)

    tensor_cuda = tensor_cpu.to(device)
    print(f"Tensor movido para o dispositivo {device}:\n", tensor_cuda)

    result_cuda = tensor_cuda + 1
    print("Resultado após a operação no tensor:\n", result_cuda)

    result_cpu = result_cuda.to('cpu')
    print("Resultado movido de volta para o CPU:\n", result_cpu)

    assert torch.allclose(result_cpu, tensor_cpu + 1), "Os resultados não coincidem entre CPU e GPU."

