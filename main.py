from random import randint
import crypto

import torch
import syft as sy

hook = sy.TorchHook(torch)
Alice = sy.VirtualWorker(hook, id="Alice")
Bob = sy.VirtualWorker(hook, id="Bob")

workers = [Alice, Bob]
crypto_provider = sy.VirtualWorker(hook, id="crypto_provider")


def simple_encrypt_decrypt_3_party(x, Q):
    shares_on_enc_x = crypto.encrypt(x, Q)
    decrypted_x = crypto.decrypt(shares_on_enc_x, Q)

    return x == decrypted_x


def addition_3_party(x, y, Q):
    shares_on_enc_x = crypto.encrypt(x, Q)
    shares_on_enc_y = crypto.encrypt(y, Q)
    added_shares = crypto.add(shares_on_enc_x, shares_on_enc_y, Q)
    dec_added = crypto.decrypt(added_shares, Q)
    return (x+y) == dec_added


def inequality(x, y, workers, crypto_provider):
    share_x = torch.tensor([x]).share(workers[0],
                                      workers[1],
                                      crypto_provider=crypto_provider)
    share_y = torch.tensor([y]).share(workers[0],
                                      workers[1],
                                      crypto_provider=crypto_provider)
    # share_z = share_x * share_y
    share_z = share_x > share_y
    return share_z.get()


if __name__ == "__main__":
    Q = randint(1e13, 1e14) # secret-key
    x = 1
    y = 2
    assert simple_encrypt_decrypt_3_party(x, Q)
    assert addition_3_party(x, y, Q)

    result = inequality(25, 5, workers=workers,
                        crypto_provider=crypto_provider)
    pass
