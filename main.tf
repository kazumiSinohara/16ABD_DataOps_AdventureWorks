provider "google" {
  credentials = "${file("service-account.json")}"
  project = "fiapterraform"
}

resource "google_composer_environment" "test" {
  name   = "example-composer-env"
  region = "us-central1"
}
