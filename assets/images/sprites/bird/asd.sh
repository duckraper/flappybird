#!/bin/bash

SPRITES_DIR="$(pwd)"

for gif in "$SPRITES_DIR"/*.gif; do
  base_name=$(basename "$gif" .gif)
  color_name=${base_name%-*}
  
  mkdir -p "$SPRITES_DIR/$color_name"

  convert "$gif" "$SPRITES_DIR/$color_name/$base_name-%02d.png"
done
