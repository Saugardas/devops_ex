variable "yc_folder_id" {
  type        = string
  description = "Идентификатор каталога в Yandex Cloud"
}

variable "docker_image" {
  type        = string
  default     = "cr.yandex/crp5124v0vt918f05j8p/iris-api:latest"
  description = "Путь к Docker-образу в Yandex Container Registry"
}
