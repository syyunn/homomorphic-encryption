import torch
import syft as sy

hook = sy.TorchHook(torch)

bob = sy.VirtualWorker(hook, id="bob")
alice = sy.VirtualWorker(hook, id="alice")
bill = sy.VirtualWorker(hook, id="bill")

x = torch.tensor([25])
encrypted_x = x.share(bob, alice, bill)

if __name__ == "__main__":
    pass
