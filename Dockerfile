name: Build and Push Docker Image

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Get current timestamp
      id: timestamp
      run: echo "::set-output name=TIME::$(date +'%Y%m%d%H%M%S')"

    - name: Log in to GitHub Container Registry
      uses: docker/login-action@v1
      with:
        registry: ghcr.io
        username: ${{ github.repository_owner }}
        password: ${{ secrets.PERSONAL_TOKEN }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v6
      with:
        context: .
        file: ./Dockerfile
        push: true
        tags: |
          ghcr.io/${{ github.repository_owner }}/app-django:latest
          ghcr.io/${{ github.repository_owner }}/app-django:${{ steps.timestamp.outputs.TIME }}