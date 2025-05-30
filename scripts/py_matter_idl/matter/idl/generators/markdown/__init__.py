# Copyright (c) 2023 Project CHIP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from matter.idl.generators import CodeGenerator, GeneratorStorage
from matter.idl.matter_idl_types import Idl


class SummaryMarkdownGenerator(CodeGenerator):
    """
    Code generation for markdown files
    """

    def __init__(self, storage: GeneratorStorage, idl: Idl, **kargs):
        super().__init__(storage, idl, fs_loader_searchpath=os.path.dirname(__file__))

    def internal_render_all(self):
        self.internal_render_one_output(
            template_path="clusters_markdown.jinja",
            output_file_name="zap_clusters.md",
            vars={
                'idl': self.idl,
            }
        )
