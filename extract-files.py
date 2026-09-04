#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/oneplus/sm8150-common',
]

blob_fixups: blob_fixups_user_type = {
    'odm/lib/hw/audio.primary.msmnile.so': blob_fixup()
        .replace_needed('/vendor/lib/liba2dpoffload.so', '/odm/lib/liba2dpoffload.so')
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so')
        .sig_replace(
            'f4 0f 9f e5 00 00 9f e7 00 00 90 e5 00 00 50 e3 b5 05 00 1a',
            'e8009ae5010710e31000a0130c018a1500f020e3',
        )
        .sig_replace(
            '08 29 9f e5 03 00 a0 e3 04 39 9f e5 06 10 a0 e1 '
            '02 20 8f e0 03 30 8f e0 25 2f 00 eb 01 00 a0 e3 '
            '4c 10 a0 e3 e2 31 00 eb 00 00 50 e3 03 01 00 0a '
            '00 80 a0 e1 bc 00 9b e5',
            'a4 00 8b e2 d6 33 00 eb 00 00 50 e3 13 01 00 1a '
            'bc 70 9b e5 00 00 57 e3 1e 00 00 0a 01 00 a0 e3 '
            '4c 10 a0 e3 e2 31 00 eb 00 00 50 e3 19 00 00 0a '
            '00 80 a0 e1 07 00 a0 e1',
        )
        .sig_replace(
            'a0 78 9f e5 a0 28 9f e5 a0 38 9f e5 07 70 8f e0 '
            '02 20 8f e0 00 00 8d e5 03 30 8f e0 03 00 a0 e3 '
            '07 10 a0 e1 01 2f 00 eb',
            'a4 00 8b e2 b1 2f 00 eb 98 78 9f e5 07 70 8f e0 '
            '04 00 00 ea a4 00 8b e2 ac 2f 00 eb e6 00 00 ea '
            '00 00 a0 e1 00 00 a0 e1',
        )
}  # fmt: skip

module = ExtractUtilsModule(
    'guacamoleb',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8150-common', module.vendor
    )
    utils.run()
