URL=https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz
ARCHIVE_DATA_PATH="CaliforniaHousing/cal_housing.data"
SAVE_DIR_PATH="data/datasets"

mkdir -p $SAVE_DIR_PATH
curl $URL -o - | tar -xz -C $SAVE_DIR_PATH --strip-components 1 -- $ARCHIVE_DATA_PATH