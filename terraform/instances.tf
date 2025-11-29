resource "yandex_compute_instance" "iris-vm" {
  name        = "iris-api-vm"
  platform_id = "standard-v2"
  zone        = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd80ok8sil1fn2gqbm6h"  # Ubuntu 22.04 LTS
      size     = 20
      type     = "network-hdd"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/yc-tf.pub")}"
    user_data = <<-EOF
      package_update: true
      package_upgrade: true
      packages:
        - apt-transport-https
        - ca-certificates
        - curl
    EOF
  }
}
