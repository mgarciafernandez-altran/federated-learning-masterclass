import torch
import syft.grid.clients.data_centric_fl_client
import syft.grid.private_grid

if __name__ == '__main__':

    hook = syft.TorchHook(torch=torch)

    worker1 = syft.grid.clients.data_centric_fl_client.DataCentricFLClient(hook=hook,
                                                                           address='http://localhost:7080/')
    worker2 = syft.grid.clients.data_centric_fl_client.DataCentricFLClient(hook=hook,
                                                                           address='http://localhost:7081/')

    grid = syft.grid.private_grid.PrivateGridNetwork(worker1, worker2)

    central_tensor  = torch.tensor([1, 2, 3, 4, 5])

    query1 = grid.search('tensor1')
    print(query1)

    print('#####')

    query2 = grid.search('tensor2')
    print(query2)

    print('#####')

    tensor1 = query1['worker-1'][0]
    tensor2 = query2['worker-2'][0]

    print('#####')

    pointer_central_1 = central_tensor.send(tensor1.location)
    result1 = tensor1 + pointer_central_1
    print(result1)
    print(result1.get())

    pointer_central_2 = central_tensor.send(tensor2.location)
    result2 = tensor2 + pointer_central_2
    print(result2)
    print(result2.get())
