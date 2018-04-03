#!/bin/bash
#sed s/置換前/置換後/  最初に見つけたMatchのみ処理
#sed s/置換前/置換後/g 各行繰り返し処理
sed -e 's/<tab>/<space>/g'