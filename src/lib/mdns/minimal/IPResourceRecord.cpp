/*
 *
 *    Copyright (c) 2020 Project CHIP Authors
 *
 *    Licensed under the Apache License, Version 2.0 (the "License");
 *    you may not use this file except in compliance with the License.
 *    You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing, software
 *    distributed under the License is distributed on an "AS IS" BASIS,
 *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *    See the License for the specific language governing permissions and
 *    limitations under the License.
 */

#include "IPResourceRecord.h"

namespace mdns {
namespace Minimal {

bool IPResourceRecord::WriteData(chip::BufBound & out) const
{
    // IP address is already stored in network byte order. We cannot use
    // PutBE/PutLE

    if (mIPAddress.IsIPv6())
    {
        out.Put(mIPAddress.Addr, 16);
    }
    else
    {
        out.Put(mIPAddress.Addr + 3, 4);
    }

    return out.Fit();
}

} // namespace Minimal
} // namespace mdns
