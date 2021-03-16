import torch
import syft.grid.clients.data_centric_fl_client

if __name__ == '__main__':

    hook = syft.TorchHook(torch=torch)

    tensor1 = torch.tensor([1, 2, 3, 4, 5])

    edge_node1 = syft.grid.clients.data_centric_fl_client.DataCentricFLClient(hook=hook,
                                                                              address='http://localhost:7080/',
                                                                              is_client_worker=True,
                                                                              verbose=True)

    print(tensor1)
    pointer = tensor1.tag('tensor1').send(edge_node1)
    print(pointer)
    edge_node1.close()