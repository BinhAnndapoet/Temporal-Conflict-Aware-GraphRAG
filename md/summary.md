# Temporal-Conflict-Aware-GraphRAG — Detailed File Summary

Tài liệu này được tạo tự động từ toàn bộ **git-tracked files** trong repo để mô tả vai trò theo từng folder và từng file.

## 1) Tổng quan nhanh

- Tổng số file tracked: **671**
- Tổng số folder có file: **168**
- Ghi chú: phần “Được gọi bởi file nào” dùng phân tích tĩnh theo tên symbol (xấp xỉ), không thay thế runtime trace.

## 2) Nhóm thư mục: `.`

### Thư mục con: `.`

- Số file: **4**

#### File: `.gitignore`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 1
- **Heading chính**: # Temporal-Conflict-Aware-GraphRAG
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 254
- **Key cấu hình chính**: name, classifiers, version, description, authors, requires-python, dev, package, members, graphrag-chunking, graphrag-common, graphrag-input, graphrag-storage, graphrag-cache, graphrag-vectors, graphrag-llm, _sort_imports, _format_code, _ruff_check, _pyright
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `uv.lock`
- **Loại**: config/data
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 4414
- **Key cấu hình chính**: version, revision, requires-python, resolution-markers, members, name, version, source, sdist, wheels, name, version, source, sdist, wheels, name, version, source, dependencies, sdist
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

## 2) Nhóm thư mục: `packages`

### Thư mục con: `packages/graphrag`

- Số file: **2**

#### File: `packages/graphrag/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 77
- **Heading chính**: # GraphRAG, ## Overview, ## Quickstart, ## Repository Guidance, ## Diving Deeper, ## Prompt Tuning, ## Versioning, ## Responsible AI FAQ
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 72
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, graphrag, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-cache`

- Số file: **2**

#### File: `packages/graphrag-cache/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 42
- **Heading chính**: # GraphRAG Cache, ### Basic, ### Custom Cache, #### Details, # cache_factory has no preregistered providers so you must register any, # providers you plan on using., # May also register a custom implementation, see above for example.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 44
- **Key cấu hình chính**: name, version, description, authors, license, readme, license-files, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-cache/example_notebooks`

- Số file: **2**

#### File: `packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-cache/graphrag_cache`

- Số file: **10**

#### File: `packages/graphrag-cache/graphrag_cache/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 21
- **Mô tả module**: The GraphRAG Cache package.
- **Imports nổi bật**: graphrag_cache.cache (Cache), graphrag_cache.cache_config (CacheConfig), graphrag_cache.cache_factory (create_cache, register_cache), graphrag_cache.cache_key (CacheKeyCreator, create_cache_key), graphrag_cache.cache_type (CacheType)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/cache.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 75
- **Mô tả module**: Abstract base class for cache.
- **Imports nổi bật**: __future__ (annotations), abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `Cache`
    - Mục đích: Provide a cache interface for the pipeline.
    - Methods chính: __init__, get, set, has, delete, clear, child
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-cache/graphrag_cache/cache_config.py, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-cache/graphrag_cache/json_cache.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/cache_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 27
- **Mô tả module**: Cache configuration model.
- **Imports nổi bật**: graphrag_storage (StorageConfig, StorageType), pydantic (BaseModel, ConfigDict, Field), graphrag_cache.cache_type (CacheType)
- **Class top-level**:
  - `CacheConfig`
    - Mục đích: The configuration section for cache.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-llm/notebooks/05_caching.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/cache_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 90
- **Mô tả module**: Cache factory implementation.
- **Imports nổi bật**: collections.abc (Callable), graphrag_common.factory (Factory, ServiceScope), graphrag_storage (Storage, create_storage), graphrag_cache.cache (Cache), graphrag_cache.cache_config (CacheConfig), graphrag_cache.cache_type (CacheType)
- **Hàm top-level**:
  - `register_cache(cache_type, cache_initializer, scope) -> None`
    - Mục đích: Register a custom cache implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, tests/integration/cache/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_cache(config, storage) -> 'Cache'`
    - Mục đích: Create a cache implementation based on the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-llm/notebooks/08_batching.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `CacheFactory`
    - Mục đích: A factory class for cache implementations.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/cache/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/cache_key.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 37
- **Mô tả module**: Create cache key.
- **Imports nổi bật**: typing (Any, Protocol, runtime_checkable), graphrag_common.hasher (hash_data)
- **Hàm top-level**:
  - `create_cache_key(input_args) -> str`
    - Mục đích: Create a cache key based on the input arguments.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-llm/graphrag_llm/cache/__init__.py, packages/graphrag-llm/graphrag_llm/cache/create_cache_key.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `CacheKeyCreator`
    - Mục đích: Create cache key function protocol.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/cache_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 16
- **Mô tả module**: Builtin cache implementation types.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `CacheType`
    - Mục đích: Enum for cache types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-cache/graphrag_cache/cache_config.py, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-llm/notebooks/05_caching.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/json_cache.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 73
- **Mô tả module**: A module containing 'JsonCache' model.
- **Imports nổi bật**: json, typing (Any), graphrag_storage (Storage, StorageConfig, create_storage), graphrag_cache.cache (Cache)
- **Class top-level**:
  - `JsonCache`
    - Mục đích: File pipeline cache class definition.
    - Methods chính: __init__, get, set, has, delete, clear, child
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/cache_factory.py, tests/integration/cache/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/memory_cache.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 70
- **Mô tả module**: MemoryCache implementation.
- **Imports nổi bật**: typing (Any), graphrag_cache.cache (Cache)
- **Class top-level**:
  - `MemoryCache`
    - Mục đích: In memory cache class definition.
    - Methods chính: __init__, get, set, has, delete, clear, child
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag/graphrag/index/run/utils.py, tests/integration/cache/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/noop_cache.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 69
- **Mô tả module**: NoopCache implementation.
- **Imports nổi bật**: typing (Any), graphrag_cache.cache (Cache)
- **Class top-level**:
  - `NoopCache`
    - Mục đích: A no-op implementation of Cache, usually useful for testing.
    - Methods chính: __init__, get, set, has, delete, clear, child
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/graphrag_cache/cache_factory.py, tests/integration/cache/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-cache/graphrag_cache/py.typed`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-chunking`

- Số file: **2**

#### File: `packages/graphrag-chunking/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 25
- **Heading chính**: # GraphRAG Chunking, ## Examples, ### Basic sentence chunking with nltk, ### Token chunking, ### Using the factory via helper util
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 44
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-chunking/example_notebooks`

- Số file: **3**

#### File: `packages/graphrag-chunking/example_notebooks/basic_sentence_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/example_notebooks/factory_helper_util_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/example_notebooks/token_chunking_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-chunking/graphrag_chunking`

- Số file: **11**

#### File: `packages/graphrag-chunking/graphrag_chunking/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: System-level chunking package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/bootstrap_nltk.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 32
- **Mô tả module**: Bootstrap definition.
- **Imports nổi bật**: warnings
- **Hàm top-level**:
  - `bootstrap()`
    - Mục đích: Bootstrap definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/graphrag_chunking/sentence_chunker.py, tests/unit/chunking/test_chunker.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/chunk_strategy_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 14
- **Mô tả module**: Chunk strategy type enumeration.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `ChunkerType`
    - Mục đích: ChunkerType class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/graphrag_chunking/chunker_factory.py, packages/graphrag-chunking/graphrag_chunking/chunking_config.py, packages/graphrag/graphrag/config/defaults.py, tests/unit/chunking/test_chunker.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/chunker.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 25
- **Mô tả module**: A module containing the 'Chunker' class.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (Callable), typing (Any), graphrag_chunking.text_chunk (TextChunk)
- **Class top-level**:
  - `Chunker`
    - Mục đích: Abstract base class for document chunkers.
    - Methods chính: __init__, chunk
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/graphrag_chunking/chunker_factory.py, packages/graphrag-chunking/graphrag_chunking/sentence_chunker.py, packages/graphrag-chunking/graphrag_chunking/token_chunker.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/chunker_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 78
- **Mô tả module**: A module containing 'ChunkerFactory', 'register_chunker', and 'create_chunker'.
- **Imports nổi bật**: collections.abc (Callable), graphrag_common.factory.factory (Factory, ServiceScope), graphrag_chunking.chunk_strategy_type (ChunkerType), graphrag_chunking.chunker (Chunker), graphrag_chunking.chunking_config (ChunkingConfig)
- **Hàm top-level**:
  - `register_chunker(chunker_type, chunker_initializer, scope) -> None`
    - Mục đích: Register a custom chunker implementation.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_chunker(config, encode, decode) -> Chunker`
    - Mục đích: Create a chunker implementation based on the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/README.md, packages/graphrag-chunking/example_notebooks/factory_helper_util_example.ipynb, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/prompt_tune/loader/input.py, tests/unit/chunking/test_chunker.py, tests/unit/prompt_tune/test_load_docs_in_chunks.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ChunkerFactory`
    - Mục đích: Factory for creating Chunker instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/chunking_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 37
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field), graphrag_chunking.chunk_strategy_type (ChunkerType)
- **Class top-level**:
  - `ChunkingConfig`
    - Mục đích: Configuration section for chunking.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/README.md, packages/graphrag-chunking/example_notebooks/factory_helper_util_example.ipynb, packages/graphrag-chunking/graphrag_chunking/chunker_factory.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/chunking/test_chunker.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/create_chunk_results.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 33
- **Mô tả module**: A module containing 'create_chunk_results' function.
- **Imports nổi bật**: collections.abc (Callable), graphrag_chunking.text_chunk (TextChunk)
- **Hàm top-level**:
  - `create_chunk_results(chunks, transform, encode) -> list[TextChunk]`
    - Mục đích: Create chunk results from a list of text chunks. The index assignments are 0-based and assume chunks were not stripped relative to the source text.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/graphrag_chunking/sentence_chunker.py, packages/graphrag-chunking/graphrag_chunking/token_chunker.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/sentence_chunker.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 49
- **Mô tả module**: A module containing 'SentenceChunker' class.
- **Imports nổi bật**: collections.abc (Callable), typing (Any), nltk, graphrag_chunking.bootstrap_nltk (bootstrap), graphrag_chunking.chunker (Chunker), graphrag_chunking.create_chunk_results (create_chunk_results), graphrag_chunking.text_chunk (TextChunk)
- **Class top-level**:
  - `SentenceChunker`
    - Mục đích: A chunker that splits text into sentence-based chunks.
    - Methods chính: __init__, chunk
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/README.md, packages/graphrag-chunking/example_notebooks/basic_sentence_example.ipynb, packages/graphrag-chunking/graphrag_chunking/chunker_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/text_chunk.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 30
- **Mô tả module**: The TextChunk dataclass.
- **Imports nổi bật**: dataclasses (dataclass)
- **Class top-level**:
  - `TextChunk`
    - Mục đích: Result of chunking a document.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/example_notebooks/factory_helper_util_example.ipynb, packages/graphrag-chunking/example_notebooks/token_chunking_example.ipynb, packages/graphrag-chunking/graphrag_chunking/chunker.py, packages/graphrag-chunking/graphrag_chunking/create_chunk_results.py, packages/graphrag-chunking/graphrag_chunking/sentence_chunker.py, packages/graphrag-chunking/graphrag_chunking/token_chunker.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/token_chunker.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 70
- **Mô tả module**: A module containing 'TokenChunker' class.
- **Imports nổi bật**: collections.abc (Callable), typing (Any), graphrag_chunking.chunker (Chunker), graphrag_chunking.create_chunk_results (create_chunk_results), graphrag_chunking.text_chunk (TextChunk)
- **Hàm top-level**:
  - `split_text_on_tokens(text, chunk_size, chunk_overlap, encode, decode) -> list[str]`
    - Mục đích: Split a single text and return chunks using the tokenizer.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py, tests/unit/chunking/test_chunker.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TokenChunker`
    - Mục đích: A chunker that splits text into token-based chunks.
    - Methods chính: __init__, chunk
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/README.md, packages/graphrag-chunking/example_notebooks/token_chunking_example.ipynb, packages/graphrag-chunking/graphrag_chunking/chunker_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-chunking/graphrag_chunking/transformers.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 26
- **Mô tả module**: A collection of useful built-in transformers you can use for chunking.
- **Imports nổi bật**: collections.abc (Callable), typing (Any)
- **Hàm top-level**:
  - `add_metadata(metadata, delimiter, line_delimiter, append) -> Callable[[str], str]`
    - Mục đích: Add metadata to the given text, prepending by default. This utility writes the dict as rows of key/value pairs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_base_text_units.py, tests/unit/chunking/test_prepend_metadata.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common`

- Số file: **2**

#### File: `packages/graphrag-common/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 16
- **Heading chính**: # GraphRAG Common, ## Factory module, ## Config module
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 45
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/example_notebooks`

- Số file: **2**

#### File: `packages/graphrag-common/example_notebooks/config_module_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 9 cells (code=5, markdown=4)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/example_notebooks/factory_module_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 5 cells (code=4, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/example_notebooks/config_files`

- Số file: **3**

#### File: `packages/graphrag-common/example_notebooks/config_files/config.toml`
- **Loại**: config/data
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Số dòng**: 6
- **Key cấu hình chính**: name, directory, filename
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/example_notebooks/config_files/config.yaml`
- **Loại**: config/data
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Số dòng**: 5
- **Key cấu hình chính**: name, logging, directory
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/example_notebooks/config_files/settings.yaml`
- **Loại**: config/data
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Số dòng**: 10
- **Key cấu hình chính**: name, logging, directory, filename
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/graphrag_common`

- Số file: **2**

#### File: `packages/graphrag-common/graphrag_common/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: GraphRAG Common package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/graphrag_common/py.typed`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/graphrag_common/config`

- Số file: **2**

#### File: `packages/graphrag-common/graphrag_common/config/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: The GraphRAG config module.
- **Imports nổi bật**: graphrag_common.config.load_config (ConfigParsingError, load_config)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/graphrag_common/config/load_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 206
- **Mô tả module**: Load configuration.
- **Imports nổi bật**: json, os, collections.abc (Callable), pathlib (Path), string (Template), typing (Any, TypeVar), yaml, dotenv (load_dotenv)
- **Hàm top-level**:
  - `_get_config_file_path(config_dir_or_file) -> Path`
    - Mục đích: Resolve the config path from the given directory or file.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_load_dotenv(env_file_path, required) -> None`
    - Mục đích: Load the .env file if it exists.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_parse_json(data) -> dict[str, Any]`
    - Mục đích: Parse JSON data.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_parse_yaml(data) -> dict[str, Any]`
    - Mục đích: Parse YAML data.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_parser_for_file(file_path) -> Callable[[str], dict[str, Any]]`
    - Mục đích: Get the parser for the given file path.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_parse_env_variables(text) -> str`
    - Mục đích: Parse environment variables in the configuration text.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_recursive_merge_dicts(dest, src) -> None`
    - Mục đích: Recursively merge two dictionaries in place.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_config(config_initializer, config_path, overrides, set_cwd, parse_env_vars, load_dot_env_file, dot_env_path, config_parser, file_encoding) -> T`
    - Mục đích: Load configuration from a file.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-common/README.md, packages/graphrag-common/example_notebooks/config_module_example.ipynb, packages/graphrag-common/graphrag_common/config/__init__.py, packages/graphrag/graphrag/cli/index.py, packages/graphrag/graphrag/cli/prompt_tune.py, packages/graphrag/graphrag/cli/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ConfigParsingError`
    - Mục đích: Configuration Parsing Error.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-common/graphrag_common/config/__init__.py, packages/graphrag/graphrag/config/load_config.py, tests/unit/load_config/test_load_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/graphrag_common/factory`

- Số file: **2**

#### File: `packages/graphrag-common/graphrag_common/factory/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: The GraphRAG factory module.
- **Imports nổi bật**: graphrag_common.factory.factory (Factory, ServiceScope)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/graphrag_common/factory/factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 114
- **Mô tả module**: Factory ABC.
- **Imports nổi bật**: abc (ABC), collections.abc (Callable), dataclasses (dataclass), typing (Any, ClassVar, Generic, Literal, TypeVar), graphrag_common.hasher (hash_data)
- **Class top-level**:
  - `_ServiceDescriptor`
    - Mục đích: Descriptor for a service.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `Factory`
    - Mục đích: Abstract base class for factories.
    - Methods chính: __new__, __init__, __contains__, keys, register, create
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-chunking/graphrag_chunking/chunker_factory.py, packages/graphrag-common/README.md, packages/graphrag-common/example_notebooks/factory_module_example.ipynb, packages/graphrag-common/graphrag_common/factory/__init__.py, packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-common/graphrag_common/hasher`

- Số file: **2**

#### File: `packages/graphrag-common/graphrag_common/hasher/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 19
- **Mô tả module**: The GraphRAG hasher module.
- **Imports nổi bật**: graphrag_common.hasher.hasher (Hasher, hash_data, make_yaml_serializable, sha256_hasher)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-common/graphrag_common/hasher/hasher.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 60
- **Mô tả module**: The GraphRAG hasher module.
- **Imports nổi bật**: hashlib, collections.abc (Callable), typing (Any), yaml
- **Hàm top-level**:
  - `sha256_hasher(data) -> str`
    - Mục đích: Generate a SHA-256 hash for the input data.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-common/graphrag_common/hasher/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `make_yaml_serializable(data) -> Any`
    - Mục đích: Convert data to a YAML-serializable format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-common/graphrag_common/hasher/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `hash_data(data) -> str`
    - Mục đích: Hash the input data dictionary using the specified hasher function.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/graphrag_cache/cache_key.py, packages/graphrag-common/graphrag_common/factory/factory.py, packages/graphrag-common/graphrag_common/hasher/__init__.py, tests/unit/hasher/test_hasher.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-input`

- Số file: **2**

#### File: `packages/graphrag-input/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 42
- **Heading chính**: # GraphRAG Inputs, ## Supported File Types, ### Markitdown Support, ## Examples
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 46
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-input/example_notebooks`

- Số file: **1**

#### File: `packages/graphrag-input/example_notebooks/input_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 6 cells (code=4, markdown=2)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-input/example_notebooks/input`

- Số file: **2**

#### File: `packages/graphrag-input/example_notebooks/input/input.csv`
- **Loại**: other
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/example_notebooks/input/input.pdf`
- **Loại**: other
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-input/graphrag_input`

- Số file: **14**

#### File: `packages/graphrag-input/graphrag_input/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 21
- **Mô tả module**: GraphRAG input document loading package.
- **Imports nổi bật**: graphrag_input.get_property (get_property), graphrag_input.input_config (InputConfig), graphrag_input.input_reader (InputReader), graphrag_input.input_reader_factory (create_input_reader), graphrag_input.input_type (InputType), graphrag_input.text_document (TextDocument)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/csv.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 46
- **Mô tả module**: A module containing 'CSVFileReader' model.
- **Imports nổi bật**: csv, io, logging, sys, graphrag_input.structured_file_reader (StructuredFileReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `CSVFileReader`
    - Mục đích: Reader implementation for csv files.
    - Methods chính: __init__, read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/get_property.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 37
- **Mô tả module**: Utility for retrieving properties from nested dictionaries.
- **Imports nổi bật**: typing (Any)
- **Hàm top-level**:
  - `get_property(data, path) -> Any`
    - Mục đích: Retrieve a property from a dictionary using dot notation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag-input/graphrag_input/structured_file_reader.py, packages/graphrag-input/graphrag_input/text_document.py, tests/unit/indexing/input/test_text_document.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/hashing.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 28
- **Mô tả module**: Hashing utilities.
- **Imports nổi bật**: collections.abc (Iterable), hashlib (sha512), typing (Any)
- **Hàm top-level**:
  - `gen_sha512_hash(item, hashcode) -> str`
    - Mục đích: Generate a SHA512 hash.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/markitdown.py, packages/graphrag-input/graphrag_input/structured_file_reader.py, packages/graphrag-input/graphrag_input/text.py, packages/graphrag/graphrag/index/operations/build_noun_graph/build_noun_graph.py, packages/graphrag/graphrag/index/operations/finalize_community_reports.py, packages/graphrag/graphrag/index/utils/hashing.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/input_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 41
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field), graphrag_input.input_type (InputType)
- **Class top-level**:
  - `InputConfig`
    - Mục đích: The default configuration section for Input.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag-input/graphrag_input/input_reader_factory.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py, tests/unit/indexing/input/test_csv_loader.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/input_reader.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 88
- **Mô tả module**: A module containing 'InputReader' model.
- **Imports nổi bật**: __future__ (annotations), logging, re, abc (ABCMeta, abstractmethod), typing (TYPE_CHECKING)
- **Class top-level**:
  - `InputReader`
    - Mục đích: Provide a cache interface for the pipeline.
    - Methods chính: __init__, read_files, __aiter__, _iterate_files, read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag-input/graphrag_input/input_reader_factory.py, packages/graphrag-input/graphrag_input/markitdown.py, packages/graphrag-input/graphrag_input/structured_file_reader.py, packages/graphrag-input/graphrag_input/text.py, packages/graphrag/graphrag/index/workflows/load_input_documents.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/input_reader_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 91
- **Mô tả module**: A module containing 'InputReaderFactory' model.
- **Imports nổi bật**: logging, collections.abc (Callable), graphrag_common.factory (Factory), graphrag_common.factory.factory (ServiceScope), graphrag_storage.storage (Storage), graphrag_input.input_config (InputConfig), graphrag_input.input_reader (InputReader), graphrag_input.input_type (InputType)
- **Hàm top-level**:
  - `register_input_reader(input_reader_type, input_reader_initializer, scope) -> None`
    - Mục đích: Register a custom input reader implementation.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_input_reader(config, storage) -> InputReader`
    - Mục đích: Create an input reader implementation based on the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag/graphrag/index/workflows/load_input_documents.py, packages/graphrag/graphrag/index/workflows/load_update_documents.py, packages/graphrag/graphrag/prompt_tune/loader/input.py, tests/unit/indexing/input/test_csv_loader.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `InputReaderFactory`
    - Mục đích: Factory for creating Input Reader instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/input_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 26
- **Mô tả module**: A module containing input file type enum.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `InputType`
    - Mục đích: The input file type for the pipeline.
    - Methods chính: __repr__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/README.md, packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag-input/graphrag_input/input_config.py, packages/graphrag-input/graphrag_input/input_reader_factory.py, packages/graphrag/graphrag/config/defaults.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/json.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 39
- **Mô tả module**: A module containing 'JSONFileReader' model.
- **Imports nổi bật**: json, logging, graphrag_input.structured_file_reader (StructuredFileReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `JSONFileReader`
    - Mục đích: Reader implementation for json files.
    - Methods chính: __init__, read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/jsonl.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 39
- **Mô tả module**: A module containing 'JSONLinesFileReader' model.
- **Imports nổi bật**: json, logging, graphrag_input.structured_file_reader (StructuredFileReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `JSONLinesFileReader`
    - Mục đích: Reader implementation for json lines files.
    - Methods chính: __init__, read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/markitdown.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 50
- **Mô tả module**: A module containing 'TextFileReader' model.
- **Imports nổi bật**: logging, io (BytesIO), pathlib (Path), markitdown (MarkItDown, StreamInfo), graphrag_input.hashing (gen_sha512_hash), graphrag_input.input_reader (InputReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `MarkItDownFileReader`
    - Mục đích: Reader implementation for any file type supported by markitdown.
    - Methods chính: read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/structured_file_reader.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 66
- **Mô tả module**: A module containing 'StructuredFileReader' model.
- **Imports nổi bật**: logging, typing (Any), graphrag_input.get_property (get_property), graphrag_input.hashing (gen_sha512_hash), graphrag_input.input_reader (InputReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `StructuredFileReader`
    - Mục đích: Base reader implementation for structured files such as csv and json.
    - Methods chính: __init__, process_data_columns
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/csv.py, packages/graphrag-input/graphrag_input/json.py, packages/graphrag-input/graphrag_input/jsonl.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/text.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 44
- **Mô tả module**: A module containing 'TextFileReader' model.
- **Imports nổi bật**: logging, pathlib (Path), graphrag_input.hashing (gen_sha512_hash), graphrag_input.input_reader (InputReader), graphrag_input.text_document (TextDocument)
- **Class top-level**:
  - `TextFileReader`
    - Mục đích: Reader implementation for text files.
    - Methods chính: __init__, read_file
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/input_reader_factory.py, packages/graphrag-input/graphrag_input/markitdown.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-input/graphrag_input/text_document.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 60
- **Mô tả module**: TextDocument dataclass.
- **Imports nổi bật**: logging, dataclasses (dataclass), typing (Any), graphrag_input.get_property (get_property)
- **Class top-level**:
  - `TextDocument`
    - Mục đích: The TextDocument holds relevant content for GraphRAG indexing.
    - Methods chính: get, collect
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/__init__.py, packages/graphrag-input/graphrag_input/csv.py, packages/graphrag-input/graphrag_input/input_reader.py, packages/graphrag-input/graphrag_input/json.py, packages/graphrag-input/graphrag_input/jsonl.py, packages/graphrag-input/graphrag_input/markitdown.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm`

- Số file: **2**

#### File: `packages/graphrag-llm/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 16
- **Heading chính**: # GraphRAG LLM, ## Basic Completion, ## Basic Embedding
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 51
- **Key cấu hình chính**: name, version, description, authors, license, readme, license-files, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/example_notebooks`

- Số file: **2**

#### File: `packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm`

- Số file: **3**

#### File: `packages/graphrag-llm/graphrag_llm/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 83
- **Heading chính**: # GraphRAG LLM, ## Basic Completion, # Streaming response, # Non-streaming response, # Alternatively, you can use the utility function to gather the full response, # The following is equivalent to the above logic. If all you care about is, # the first choice response then you can use the gather_completion_response, # utility function.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: GraphRAG LLM Package.
- **Imports nổi bật**: nest_asyncio2
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/py.typed`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/cache`

- Số file: **2**

#### File: `packages/graphrag-llm/graphrag_llm/cache/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 11
- **Mô tả module**: Cache module.
- **Imports nổi bật**: graphrag_llm.cache.create_cache_key (create_cache_key)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/cache/create_cache_key.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 72
- **Mô tả module**: Create cache key.
- **Imports nổi bật**: typing (Any), graphrag_cache (create_cache_key)
- **Hàm top-level**:
  - `create_cache_key(input_args) -> str`
    - Mục đích: Generate a cache key based on the model configuration and input arguments.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-cache/graphrag_cache/cache_key.py, packages/graphrag-llm/graphrag_llm/cache/__init__.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_parameters(input_args) -> dict[str, Any]`
    - Mục đích: Pluck out the parameters that define a cache key.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/completion`

- Số file: **5**

#### File: `packages/graphrag-llm/graphrag_llm/completion/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: Completion module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.completion.completion (LLMCompletion), graphrag_llm.completion.completion_factory (create_completion, register_completion)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/completion/completion.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 266
- **Mô tả module**: Completion Abstract Base Class.
- **Imports nổi bật**: abc (ABC, abstractmethod), contextlib (contextmanager), typing (TYPE_CHECKING, Any, Unpack), graphrag_llm.threading.completion_thread_runner (completion_thread_runner)
- **Class top-level**:
  - `LLMCompletion`
    - Mục đích: Abstract base class for language model completions.
    - Methods chính: __init__, completion, completion_async, completion_thread_pool, completion_batch, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/completion/__init__.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/completion/completion_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 151
- **Mô tả module**: Completion factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING, Any), graphrag_common.factory (Factory), graphrag_llm.cache (create_cache_key), graphrag_llm.config.tokenizer_config (TokenizerConfig), graphrag_llm.config.types (LLMProviderType), graphrag_llm.metrics.noop_metrics_store (NoopMetricsStore), graphrag_llm.tokenizer.tokenizer_factory (create_tokenizer)
- **Hàm top-level**:
  - `register_completion(completion_type, completion_initializer, scope) -> None`
    - Mục đích: Register a custom completion implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/__init__.py, tests/integration/language_model/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_completion(model_config) -> 'LLMCompletion'`
    - Mục đích: Create a Completion instance based on the model configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/completion/__init__.py, packages/graphrag-llm/notebooks/01_basic.ipynb, packages/graphrag-llm/notebooks/02_encoding_decoding.ipynb, packages/graphrag-llm/notebooks/03_structured_responses.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `CompletionFactory`
    - Mục đích: Factory for creating Completion instances.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 303
- **Mô tả module**: LLMCompletion based on litellm.
- **Imports nổi bật**: collections.abc (AsyncIterator, Iterator), typing (TYPE_CHECKING, Any, Unpack), litellm, azure.identity (DefaultAzureCredential, get_bearer_token_provider), litellm (ModelResponse), graphrag_llm.completion.completion (LLMCompletion), graphrag_llm.config.types (AuthMethod), graphrag_llm.middleware (with_middleware_pipeline), graphrag_llm.types (LLMCompletionChunk, LLMCompletionResponse), graphrag_llm.utils (structure_completion_response)
- **Hàm top-level**:
  - `_create_base_completions() -> tuple['LLMCompletionFunction', 'AsyncLLMCompletionFunction']`
    - Mục đích: Create base completions for LiteLLM.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `LiteLLMCompletion`
    - Mục đích: LLMCompletion based on litellm.
    - Methods chính: __init__, completion, completion_async, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 131
- **Mô tả module**: Mock LLMCompletion.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any, Unpack), litellm, graphrag_llm.completion.completion (LLMCompletion), graphrag_llm.utils (create_completion_response, structure_completion_response)
- **Class top-level**:
  - `MockLLMCompletion`
    - Mục đích: LLMCompletion based on litellm.
    - Methods chính: __init__, completion, completion_async, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/config`

- Số file: **8**

#### File: `packages/graphrag-llm/graphrag_llm/config/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 43
- **Mô tả module**: Config module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.config.metrics_config (MetricsConfig), graphrag_llm.config.model_config (ModelConfig), graphrag_llm.config.rate_limit_config (RateLimitConfig), graphrag_llm.config.retry_config (RetryConfig), graphrag_llm.config.template_engine_config (TemplateEngineConfig), graphrag_llm.config.tokenizer_config (TokenizerConfig), graphrag_llm.config.types (AuthMethod, LLMProviderType, MetricsProcessorType, MetricsStoreType, MetricsWriterType, RateLimitType, RetryType, TemplateEngineType, TemplateManagerType, TokenizerType)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/metrics_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 58
- **Mô tả module**: Metrics configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.types (MetricsProcessorType, MetricsStoreType, MetricsWriterType)
- **Class top-level**:
  - `MetricsConfig`
    - Mục đích: Configuration for metrics.
    - Methods chính: _validate_file_metrics_writer_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/model_config.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_processor_factory.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_store_factory.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_writer_factory.py, packages/graphrag-llm/notebooks/04_metrics.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/model_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 112
- **Mô tả module**: Language model configuration.
- **Imports nổi bật**: logging, typing (Any), pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.metrics_config (MetricsConfig), graphrag_llm.config.rate_limit_config (RateLimitConfig), graphrag_llm.config.retry_config (RetryConfig), graphrag_llm.config.types (AuthMethod, LLMProviderType)
- **Class top-level**:
  - `ModelConfig`
    - Mục đích: Configuration for a language model.
    - Methods chính: _validate_lite_llm_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/README.md, packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/cache/create_cache_key.py, packages/graphrag-llm/graphrag_llm/completion/completion.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/rate_limit_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 61
- **Mô tả module**: RateLimit configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.types (RateLimitType)
- **Class top-level**:
  - `RateLimitConfig`
    - Mục đích: Configuration for rate limit behavior.
    - Methods chính: _validate_sliding_window_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/model_config.py, packages/graphrag-llm/graphrag_llm/rate_limit/rate_limit_factory.py, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-llm/notebooks/07_rate_limiting.ipynb, packages/graphrag-llm/notebooks/08_batching.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/retry_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 70
- **Mô tả module**: Retry configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.types (RetryType)
- **Class top-level**:
  - `RetryConfig`
    - Mục đích: Configuration for retry behavior.
    - Methods chính: _validate_exponential_backoff_config, _validate_immediate_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/model_config.py, packages/graphrag-llm/graphrag_llm/retry/retry_factory.py, packages/graphrag-llm/notebooks/06_retries.ipynb, tests/integration/language_model/test_retries.py, tests/unit/config/test_retry_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/template_engine_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 70
- **Mô tả module**: Template engine configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.types (TemplateEngineType, TemplateManagerType)
- **Class top-level**:
  - `TemplateEngineConfig`
    - Mục đích: Configuration for the template engine.
    - Methods chính: _validate_file_template_manager_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py, packages/graphrag-llm/graphrag_llm/templating/template_manager_factory.py, packages/graphrag-llm/notebooks/11_templating.ipynb, tests/unit/config/test_template_engine_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/tokenizer_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 52
- **Mô tả module**: Tokenizer model configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field, model_validator), graphrag_llm.config.types (TokenizerType)
- **Class top-level**:
  - `TokenizerConfig`
    - Mục đích: Configuration for a tokenizer.
    - Methods chính: _validate_litellm_config, _validate_tiktoken_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer_factory.py, packages/graphrag-llm/notebooks/02_encoding_decoding.ipynb, packages/graphrag/graphrag/tokenizer/get_tokenizer.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/config/types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 73
- **Mô tả module**: GraphRAG LLM configuration types.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `LLMProviderType`
    - Mục đích: Enum for LLM provider types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/model_config.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/notebooks/12_mocking.ipynb, tests/unit/config/test_model_config.py
  - `AuthMethod`
    - Mục đích: Enum for authentication methods.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/model_config.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py
  - `MetricsProcessorType`
    - Mục đích: Enum for built-in MetricsProcessor types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_processor_factory.py
  - `MetricsWriterType`
    - Mục đích: Enum for built-in MetricsWriter types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_writer_factory.py, packages/graphrag-llm/notebooks/04_metrics.ipynb, tests/unit/config/test_metrics_config.py
  - `MetricsStoreType`
    - Mục đích: Enum for built-in MetricsStore types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_store_factory.py
  - `RateLimitType`
    - Mục đích: Enum for built-in RateLimit types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/rate_limit_config.py, packages/graphrag-llm/graphrag_llm/rate_limit/rate_limit_factory.py, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-llm/notebooks/07_rate_limiting.ipynb, packages/graphrag-llm/notebooks/08_batching.ipynb
  - `RetryType`
    - Mục đích: Enum for built-in Retry types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/retry_config.py, packages/graphrag-llm/graphrag_llm/retry/retry_factory.py, packages/graphrag-llm/notebooks/06_retries.ipynb, tests/integration/language_model/test_retries.py, tests/unit/config/test_retry_config.py
  - `TemplateEngineType`
    - Mục đích: Enum for built-in TemplateEngine types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/template_engine_config.py, packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py, packages/graphrag-llm/notebooks/11_templating.ipynb, tests/unit/config/test_template_engine_config.py
  - `TemplateManagerType`
    - Mục đích: Enum for built-in TemplateEngine types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/template_engine_config.py, packages/graphrag-llm/graphrag_llm/templating/template_manager_factory.py, packages/graphrag-llm/notebooks/11_templating.ipynb, tests/unit/config/test_template_engine_config.py
  - `TokenizerType`
    - Mục đích: Enum for tokenizer types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/__init__.py, packages/graphrag-llm/graphrag_llm/config/tokenizer_config.py, packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer_factory.py, packages/graphrag-llm/notebooks/02_encoding_decoding.ipynb, packages/graphrag/graphrag/tokenizer/get_tokenizer.py, tests/unit/config/test_tokenizer_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/embedding`

- Số file: **5**

#### File: `packages/graphrag-llm/graphrag_llm/embedding/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: LLMEmbedding module for graphrag_llm.
- **Imports nổi bật**: graphrag_llm.embedding.embedding (LLMEmbedding), graphrag_llm.embedding.embedding_factory (create_embedding, register_embedding)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/embedding/embedding.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 192
- **Mô tả module**: Completion Abstract Base Class.
- **Imports nổi bật**: abc (ABC, abstractmethod), contextlib (contextmanager), typing (TYPE_CHECKING, Any, Unpack), graphrag_llm.threading.embedding_thread_runner (embedding_thread_runner)
- **Class top-level**:
  - `LLMEmbedding`
    - Mục đích: Abstract base class for language model embeddings.
    - Methods chính: __init__, embedding, embedding_async, embedding_thread_pool, embedding_batch, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/embedding/__init__.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/embedding/mock_llm_embedding.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 151
- **Mô tả module**: Embedding factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING, Any), graphrag_common.factory (Factory), graphrag_llm.cache (create_cache_key), graphrag_llm.config.tokenizer_config (TokenizerConfig), graphrag_llm.config.types (LLMProviderType), graphrag_llm.metrics.noop_metrics_store (NoopMetricsStore), graphrag_llm.tokenizer.tokenizer_factory (create_tokenizer)
- **Hàm top-level**:
  - `register_embedding(embedding_type, embedding_initializer, scope) -> None`
    - Mục đích: Register a custom completion implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/__init__.py, tests/integration/language_model/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_embedding(model_config) -> 'LLMEmbedding'`
    - Mục đích: Create an Embedding instance based on the model configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/embedding/__init__.py, packages/graphrag-llm/notebooks/01_basic.ipynb, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-llm/notebooks/08_batching.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `EmbeddingFactory`
    - Mục đích: Factory for creating Embedding instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 199
- **Mô tả module**: LLMEmbedding based on litellm.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any, Unpack), litellm, azure.identity (DefaultAzureCredential, get_bearer_token_provider), graphrag_llm.config.types (AuthMethod), graphrag_llm.embedding.embedding (LLMEmbedding), graphrag_llm.middleware (with_middleware_pipeline), graphrag_llm.types (LLMEmbeddingResponse)
- **Hàm top-level**:
  - `_create_base_embeddings() -> tuple['LLMEmbeddingFunction', 'AsyncLLMEmbeddingFunction']`
    - Mục đích: Create base embedding functions.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `LiteLLMEmbedding`
    - Mục đích: LLMEmbedding based on litellm.
    - Methods chính: __init__, embedding, embedding_async, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/embedding/mock_llm_embedding.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 82
- **Mô tả module**: MockLLMEmbedding.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any, Unpack), litellm, graphrag_llm.embedding.embedding (LLMEmbedding), graphrag_llm.utils (create_embedding_response)
- **Class top-level**:
  - `MockLLMEmbedding`
    - Mục đích: MockLLMEmbedding.
    - Methods chính: __init__, embedding, embedding_async, metrics_store, tokenizer
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/metrics`

- Số file: **13**

#### File: `packages/graphrag-llm/graphrag_llm/metrics/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 35
- **Mô tả module**: Metrics module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.metrics.metrics_aggregator (metrics_aggregator), graphrag_llm.metrics.metrics_processor (MetricsProcessor), graphrag_llm.metrics.metrics_processor_factory (create_metrics_processor, register_metrics_processor), graphrag_llm.metrics.metrics_store (MetricsStore), graphrag_llm.metrics.metrics_store_factory (create_metrics_store, register_metrics_store), graphrag_llm.metrics.metrics_writer (MetricsWriter), graphrag_llm.metrics.metrics_writer_factory (create_metrics_writer, register_metrics_writer)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/default_metrics_processor.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 131
- **Mô tả module**: Default Metrics Processor.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any), graphrag_llm.metrics.metrics_processor (MetricsProcessor), graphrag_llm.model_cost_registry (model_cost_registry), graphrag_llm.types (LLMCompletionResponse, LLMEmbeddingResponse)
- **Class top-level**:
  - `DefaultMetricsProcessor`
    - Mục đích: Default metrics processor that does nothing.
    - Methods chính: __init__, process_metrics, _process_metrics_common, _process_lm_chat_completion, _process_lm_embedding_response
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/metrics_processor_factory.py, packages/graphrag-llm/notebooks/04_metrics.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/file_metrics_writer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 38
- **Mô tả module**: File metrics writer implementation.
- **Imports nổi bật**: json, collections.abc (Callable), datetime (datetime, timezone), pathlib (Path), typing (TYPE_CHECKING, Any), graphrag_llm.metrics.metrics_writer (MetricsWriter)
- **Class top-level**:
  - `FileMetricsWriter`
    - Mục đích: File metrics writer implementation.
    - Methods chính: __init__, write_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/metrics_writer_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/log_metrics_writer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 40
- **Mô tả module**: Log metrics writer implementation.
- **Imports nổi bật**: json, logging, collections.abc (Callable), typing (TYPE_CHECKING, Any), graphrag_llm.metrics.metrics_writer (MetricsWriter)
- **Class top-level**:
  - `LogMetricsWriter`
    - Mục đích: Log metrics writer implementation.
    - Methods chính: __init__, write_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/metrics_writer_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/memory_metrics_store.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 113
- **Mô tả module**: Default metrics store.
- **Imports nổi bật**: atexit, threading, typing (TYPE_CHECKING, Any), graphrag_llm.metrics.metrics_aggregator (metrics_aggregator), graphrag_llm.metrics.metrics_store (MetricsStore)
- **Class top-level**:
  - `MemoryMetricsStore`
    - Mục đích: Store for metrics.
    - Methods chính: __init__, _on_exit_, id, update_metrics, _sort_metrics, get_metrics, clear_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/metrics_store_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_aggregator.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 143
- **Mô tả module**: Metrics aggregator module.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING, Any, ClassVar), typing_extensions (Self)
- **Hàm top-level**:
  - `_failure_rate(metrics) -> None`
    - Mục đích: Calculate failure rate metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_retry_rate(metrics) -> None`
    - Mục đích: Calculate failure rate metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_tokens_per_response(metrics) -> None`
    - Mục đích: Calculate tokens per response metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_cost_per_response(metrics) -> None`
    - Mục đích: Calculate cost per response metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_compute_duration_per_response(metrics) -> None`
    - Mục đích: Calculate compute duration per response metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_cache_hit_rate(metrics) -> None`
    - Mục đích: Calculate cache hit rate metric.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MetricsAggregator`
    - Mục đích: Metrics Aggregator.
    - Methods chính: __new__, __init__, register, clear, aggregate
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_processor.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 60
- **Mô tả module**: Metrics processor abstract base class.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `MetricsProcessor`
    - Mục đích: Abstract base class for metrics processors.
    - Methods chính: __init__, process_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/config/types.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_processor_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 80
- **Mô tả module**: Metrics processor factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.types (MetricsProcessorType), graphrag_llm.metrics.metrics_processor (MetricsProcessor)
- **Hàm top-level**:
  - `register_metrics_processor(processor_type, processor_initializer) -> None`
    - Mục đích: Register a custom metrics processor implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/__init__.py, packages/graphrag-llm/notebooks/04_metrics.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_metrics_processor(metrics_config) -> MetricsProcessor`
    - Mục đích: Create a MetricsProcessor instance based on the configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/metrics/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MetricsProcessorFactory`
    - Mục đích: Factory for creating MetricsProcessor instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_store.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 82
- **Mô tả module**: Metrics Store.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `MetricsStore`
    - Mục đích: Abstract base class for metrics stores.
    - Methods chính: __init__, id, update_metrics, get_metrics, clear_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/config/types.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_store_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 92
- **Mô tả module**: Metrics store factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING, Any), graphrag_common.factory (Factory), graphrag_llm.config.types (MetricsStoreType), graphrag_llm.metrics.metrics_store (MetricsStore)
- **Hàm top-level**:
  - `register_metrics_store(store_type, store_initializer, scope) -> None`
    - Mục đích: Register a custom metrics store implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_metrics_store(config, id) -> MetricsStore`
    - Mục đích: Create a MetricsStore instance based on the configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/metrics/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MetricsStoreFactory`
    - Mục đích: Factory for creating MetricsProcessor instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_writer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 33
- **Mô tả module**: Metrics writer abstract base class.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `MetricsWriter`
    - Mục đích: Abstract base class for metrics writers.
    - Methods chính: __init__, write_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/metrics_config.py, packages/graphrag-llm/graphrag_llm/config/types.py, packages/graphrag-llm/graphrag_llm/metrics/__init__.py, packages/graphrag-llm/graphrag_llm/metrics/file_metrics_writer.py, packages/graphrag-llm/graphrag_llm/metrics/log_metrics_writer.py, packages/graphrag-llm/graphrag_llm/metrics/memory_metrics_store.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/metrics_writer_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 92
- **Mô tả module**: Metrics writer factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.types (MetricsWriterType), graphrag_llm.metrics.metrics_writer (MetricsWriter)
- **Hàm top-level**:
  - `register_metrics_writer(metrics_writer_type, metrics_writer_initializer, scope) -> None`
    - Mục đích: Register a custom metrics writer implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_metrics_writer(metrics_config) -> MetricsWriter`
    - Mục đích: Create a MetricsWriter instance based on the configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/metrics/__init__.py, packages/graphrag-llm/graphrag_llm/metrics/metrics_store_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MetricsWriterFactory`
    - Mục đích: Metrics writer factory.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/metrics/noop_metrics_store.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 42
- **Mô tả module**: Noop metrics store.
- **Imports nổi bật**: typing (Any), graphrag_llm.metrics.metrics_store (MetricsStore), graphrag_llm.types (Metrics)
- **Class top-level**:
  - `NoopMetricsStore`
    - Mục đích: Noop store for metrics.
    - Methods chính: __init__, id, update_metrics, get_metrics, clear_metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/middleware`

- Số file: **9**

#### File: `packages/graphrag-llm/graphrag_llm/middleware/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 25
- **Mô tả module**: Middleware.
- **Imports nổi bật**: graphrag_llm.middleware.with_cache (with_cache), graphrag_llm.middleware.with_errors_for_testing (with_errors_for_testing), graphrag_llm.middleware.with_logging (with_logging), graphrag_llm.middleware.with_metrics (with_metrics), graphrag_llm.middleware.with_middleware_pipeline (with_middleware_pipeline), graphrag_llm.middleware.with_rate_limiting (with_rate_limiting), graphrag_llm.middleware.with_request_count (with_request_count), graphrag_llm.middleware.with_retries (with_retries)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_cache.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 154
- **Mô tả module**: Cache middleware.
- **Imports nổi bật**: asyncio, typing (TYPE_CHECKING, Any, Literal), graphrag_llm.types (LLMCompletionResponse, LLMEmbeddingResponse)
- **Hàm top-level**:
  - `with_cache() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with cache middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_errors_for_testing.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 84
- **Mô tả module**: Error testing middleware.
- **Imports nổi bật**: asyncio, random, time, typing (TYPE_CHECKING, Any), litellm.exceptions
- **Hàm top-level**:
  - `with_errors_for_testing() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with error testing middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_logging.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 74
- **Mô tả module**: Request count middleware.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING, Any)
- **Hàm top-level**:
  - `with_logging() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with logging middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_metrics.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 99
- **Mô tả module**: Metrics middleware to process metrics using a MetricsProcessor.
- **Imports nổi bật**: time, typing (TYPE_CHECKING, Any)
- **Hàm top-level**:
  - `with_metrics() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with metrics middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 155
- **Mô tả module**: Wraps model functions in middleware pipeline.
- **Imports nổi bật**: typing (TYPE_CHECKING, Literal), graphrag_llm.middleware.with_cache (with_cache), graphrag_llm.middleware.with_errors_for_testing (with_errors_for_testing), graphrag_llm.middleware.with_logging (with_logging), graphrag_llm.middleware.with_metrics (with_metrics), graphrag_llm.middleware.with_rate_limiting (with_rate_limiting), graphrag_llm.middleware.with_request_count (with_request_count), graphrag_llm.middleware.with_retries (with_retries)
- **Hàm top-level**:
  - `with_middleware_pipeline() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions in middleware pipeline.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/middleware/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_rate_limiting.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 80
- **Mô tả module**: Rate limit middleware.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any)
- **Hàm top-level**:
  - `with_rate_limiting() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with rate limit middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_request_count.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 82
- **Mô tả module**: Request count middleware.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any)
- **Hàm top-level**:
  - `with_request_count() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with request count middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/middleware/with_retries.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 61
- **Mô tả module**: Retry middleware.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any)
- **Hàm top-level**:
  - `with_retries() -> tuple['LLMFunction', 'AsyncLLMFunction']`
    - Mục đích: Wrap model functions with retry middleware.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/__init__.py, packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/model_cost_registry`

- Số file: **2**

#### File: `packages/graphrag-llm/graphrag_llm/model_cost_registry/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 12
- **Mô tả module**: Model cost registry module.
- **Imports nổi bật**: graphrag_llm.model_cost_registry.model_cost_registry (ModelCosts, model_cost_registry)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/model_cost_registry/model_cost_registry.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 66
- **Mô tả module**: Model cost registry module.
- **Imports nổi bật**: typing (Any, ClassVar, TypedDict), litellm (model_cost), typing_extensions (Self)
- **Class top-level**:
  - `ModelCosts`
    - Mục đích: Model costs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/model_cost_registry/__init__.py
  - `ModelCostRegistry`
    - Mục đích: Registry for model costs.
    - Methods chính: __new__, __init__, register_model_costs, get_model_costs
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/rate_limit`

- Số file: **4**

#### File: `packages/graphrag-llm/graphrag_llm/rate_limit/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: Rate limit module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.rate_limit.rate_limit_factory (create_rate_limiter, register_rate_limiter), graphrag_llm.rate_limit.rate_limiter (RateLimiter)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/rate_limit/rate_limit_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 85
- **Mô tả module**: Rate limit factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config (RateLimitType), graphrag_llm.rate_limit.rate_limiter (RateLimiter)
- **Hàm top-level**:
  - `register_rate_limiter(rate_limit_type, rate_limiter_initializer, scope) -> None`
    - Mục đích: Register a custom RateLimiter implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/rate_limit/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_rate_limiter(rate_limit_config) -> RateLimiter`
    - Mục đích: Create a RateLimiter instance.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/rate_limit/__init__.py, tests/integration/language_model/test_rate_limiter.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `RateLimitFactory`
    - Mục đích: Factory to create RateLimiter instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/rate_limit/rate_limiter.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 39
- **Mô tả module**: LiteLLM Rate Limiter.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (Iterator), contextlib (contextmanager), typing (Any)
- **Class top-level**:
  - `RateLimiter`
    - Mục đích: Abstract base class for rate limiters.
    - Methods chính: __init__, acquire
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/rate_limit/sliding_window_rate_limiter.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 144
- **Mô tả module**: LiteLLM Static Rate Limiter.
- **Imports nổi bật**: threading, time, collections (deque), collections.abc (Iterator), contextlib (contextmanager), typing (Any), graphrag_llm.rate_limit.rate_limiter (RateLimiter)
- **Class top-level**:
  - `SlidingWindowRateLimiter`
    - Mục đích: Sliding Window Rate Limiter implementation.
    - Methods chính: __init__, acquire
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/rate_limit/rate_limit_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/retry`

- Số file: **6**

#### File: `packages/graphrag-llm/graphrag_llm/retry/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 14
- **Mô tả module**: Retry module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.retry.retry (Retry), graphrag_llm.retry.retry_factory (create_retry, register_retry)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/retry/exceptions_to_skip.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 23
- **Mô tả module**: List of exception names to skip for retries.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/retry/exponential_retry.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 120
- **Mô tả module**: Exponential backoff retry implementation.
- **Imports nổi bật**: asyncio, random, time, collections.abc (Awaitable, Callable), typing (TYPE_CHECKING, Any), graphrag_llm.retry.exceptions_to_skip (_default_exceptions_to_skip), graphrag_llm.retry.retry (Retry)
- **Class top-level**:
  - `ExponentialRetry`
    - Mục đích: Exponential backoff retry implementation.
    - Methods chính: __init__, retry, retry_async
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/retry/retry_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/retry/immediate_retry.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 86
- **Mô tả module**: Native (immediate) retry implementation.
- **Imports nổi bật**: collections.abc (Awaitable, Callable), typing (TYPE_CHECKING, Any), graphrag_llm.retry.exceptions_to_skip (_default_exceptions_to_skip), graphrag_llm.retry.retry (Retry)
- **Class top-level**:
  - `ImmediateRetry`
    - Mục đích: Immediate retry implementation.
    - Methods chính: __init__, retry, retry_async
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/retry/retry_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/retry/retry.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 33
- **Mô tả module**: Retry abstract base class.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (Awaitable, Callable), typing (Any)
- **Class top-level**:
  - `Retry`
    - Mục đích: Retry Abstract Base Class.
    - Methods chính: __init__, retry, retry_async
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/config/retry_config.py, packages/graphrag-llm/graphrag_llm/config/types.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/retry/retry_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 87
- **Mô tả module**: Retry factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.types (RetryType), graphrag_llm.retry.retry (Retry)
- **Hàm top-level**:
  - `register_retry(retry_type, retry_initializer, scope) -> None`
    - Mục đích: Register a custom Retry implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/retry/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_retry(retry_config) -> Retry`
    - Mục đích: Create a Retry instance.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/retry/__init__.py, tests/integration/language_model/test_retries.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `RetryFactory`
    - Mục đích: Factory to create Retry instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/templating`

- Số file: **7**

#### File: `packages/graphrag-llm/graphrag_llm/templating/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 25
- **Mô tả module**: Templates module.
- **Imports nổi bật**: graphrag_llm.templating.template_engine (TemplateEngine), graphrag_llm.templating.template_engine_factory (create_template_engine, register_template_engine), graphrag_llm.templating.template_manager (TemplateManager), graphrag_llm.templating.template_manager_factory (create_template_manager, register_template_manager)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/file_template_manager.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 77
- **Mô tả module**: In-memory template manager implementation.
- **Imports nổi bật**: pathlib (Path), typing (Any), graphrag_llm.templating.template_manager (TemplateManager)
- **Class top-level**:
  - `FileTemplateManager`
    - Mục đích: Abstract base class for template managers.
    - Methods chính: __init__, get, register, keys, __contains__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/template_manager_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/jinja_template_engine.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 56
- **Mô tả module**: Jinja template engine.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any), jinja2 (StrictUndefined, Template, UndefinedError), graphrag_llm.templating.template_engine (TemplateEngine)
- **Class top-level**:
  - `JinjaTemplateEngine`
    - Mục đích: Jinja template engine.
    - Methods chính: __init__, render, template_manager
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/template_engine.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 54
- **Mô tả module**: Abstract base class for template engines.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `TemplateEngine`
    - Mục đích: Abstract base class for template engines.
    - Methods chính: __init__, render, template_manager
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/config/types.py, packages/graphrag-llm/graphrag_llm/templating/__init__.py, packages/graphrag-llm/graphrag_llm/templating/jinja_template_engine.py, packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 96
- **Mô tả module**: Template engine factory implementation.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.template_engine_config (TemplateEngineConfig), graphrag_llm.config.types (TemplateEngineType), graphrag_llm.templating.template_engine (TemplateEngine), graphrag_llm.templating.template_manager_factory (create_template_manager)
- **Hàm top-level**:
  - `register_template_engine(template_engine_type, template_engine_initializer, scope) -> None`
    - Mục đích: Register a custom template engine implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_template_engine(template_engine_config) -> TemplateEngine`
    - Mục đích: Create a TemplateEngine instance.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/__init__.py, packages/graphrag-llm/notebooks/11_templating.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TemplateEngineFactory`
    - Mục đích: Factory for creating template engine instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/template_manager.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 66
- **Mô tả module**: Abstract base class for template managers.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (Any)
- **Class top-level**:
  - `TemplateManager`
    - Mục đích: Abstract base class for template managers.
    - Methods chính: __init__, get, register, keys, __contains__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/__init__.py, packages/graphrag-llm/graphrag_llm/templating/file_template_manager.py, packages/graphrag-llm/graphrag_llm/templating/jinja_template_engine.py, packages/graphrag-llm/graphrag_llm/templating/template_engine.py, packages/graphrag-llm/graphrag_llm/templating/template_manager_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/templating/template_manager_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 83
- **Mô tả module**: Template manager factory implementation.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.template_engine_config (TemplateEngineConfig), graphrag_llm.config.types (TemplateManagerType), graphrag_llm.templating.template_manager (TemplateManager)
- **Hàm top-level**:
  - `register_template_manager(template_manager_type, template_manager_initializer, scope) -> None`
    - Mục đích: Register a custom template manager implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_template_manager(template_engine_config) -> TemplateManager`
    - Mục đích: Create a TemplateManager instance.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/templating/__init__.py, packages/graphrag-llm/graphrag_llm/templating/template_engine_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TemplateManagerFactory`
    - Mục đích: Factory for creating template manager instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/threading`

- Số file: **5**

#### File: `packages/graphrag-llm/graphrag_llm/threading/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 11
- **Mô tả module**: Threading module.
- **Imports nổi bật**: graphrag_llm.threading.completion_thread_runner (completion_thread_runner)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/threading/completion_thread.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 92
- **Mô tả module**: Completion Thread.
- **Imports nổi bật**: threading, queue (Empty, Queue), typing (TYPE_CHECKING)
- **Class top-level**:
  - `CompletionThread`
    - Mục đích: Thread for handling LLM completions.
    - Methods chính: __init__, run
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/threading/completion_thread_runner.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/threading/completion_thread_runner.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 244
- **Mô tả module**: Completion Thread Runner.
- **Imports nổi bật**: asyncio, sys, threading, time, collections.abc (Awaitable, Iterator), contextlib (contextmanager), queue (Empty, Queue), typing (TYPE_CHECKING, Protocol, Unpack, runtime_checkable), graphrag_llm.threading.completion_thread (CompletionThread)
- **Hàm top-level**:
  - `_start_completion_thread_pool() -> tuple[list[CompletionThread], 'LLMCompletionRequestQueue', 'LLMCompletionResponseQueue']`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `completion_thread_runner() -> Iterator[ThreadedLLMCompletionFunction]`
    - Mục đích: Run a completion thread pool.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/threading/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ThreadedLLMCompletionResponseHandler`
    - Mục đích: Threaded completion response handler.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py
  - `ThreadedLLMCompletionFunction`
    - Mục đích: Threaded completion function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/threading/embedding_thread.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 89
- **Mô tả module**: Embedding Thread.
- **Imports nổi bật**: threading, queue (Empty, Queue), typing (TYPE_CHECKING)
- **Class top-level**:
  - `EmbeddingThread`
    - Mục đích: Thread for handling LLM embeddings.
    - Methods chính: __init__, run
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/threading/embedding_thread_runner.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/threading/embedding_thread_runner.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 217
- **Mô tả module**: Embedding Thread Runner.
- **Imports nổi bật**: asyncio, sys, threading, time, collections.abc (Awaitable, Iterator), contextlib (contextmanager), queue (Empty, Queue), typing (TYPE_CHECKING, Protocol, Unpack, runtime_checkable), graphrag_llm.threading.embedding_thread (EmbeddingThread)
- **Hàm top-level**:
  - `_start_embedding_thread_pool() -> tuple[list['EmbeddingThread'], 'LLMEmbeddingRequestQueue', 'LLMEmbeddingResponseQueue']`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `embedding_thread_runner() -> Iterator[ThreadedLLMEmbeddingFunction]`
    - Mục đích: Run an embedding thread pool.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ThreadedLLMEmbeddingResponseHandler`
    - Mục đích: Threaded embedding response handler.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding.py
  - `ThreadedLLMEmbeddingFunction`
    - Mục đích: Threaded embedding function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/tokenizer`

- Số file: **5**

#### File: `packages/graphrag-llm/graphrag_llm/tokenizer/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: Tokenizer module.
- **Imports nổi bật**: graphrag_llm.tokenizer.tokenizer (Tokenizer), graphrag_llm.tokenizer.tokenizer_factory (create_tokenizer, register_tokenizer)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/tokenizer/lite_llm_tokenizer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 55
- **Mô tả module**: LiteLLM Tokenizer.
- **Imports nổi bật**: typing (Any), litellm (decode, encode), graphrag_llm.tokenizer.tokenizer (Tokenizer)
- **Class top-level**:
  - `LiteLLMTokenizer`
    - Mục đích: LiteLLM Tokenizer.
    - Methods chính: __init__, encode, decode
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/tokenizer/tiktoken_tokenizer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 56
- **Mô tả module**: LiteLLM Tokenizer.
- **Imports nổi bật**: typing (Any), tiktoken, graphrag_llm.tokenizer.tokenizer (Tokenizer)
- **Class top-level**:
  - `TiktokenTokenizer`
    - Mục đích: LiteLLM Tokenizer.
    - Methods chính: __init__, encode, decode
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 112
- **Mô tả module**: Tokenizer Abstract Base Class.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (TYPE_CHECKING, Any)
- **Class top-level**:
  - `Tokenizer`
    - Mục đích: Tokenizer Abstract Base Class.
    - Methods chính: __init__, encode, decode, num_prompt_tokens, num_tokens
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/config/tokenizer_config.py, packages/graphrag-llm/graphrag_llm/embedding/embedding.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/tokenizer/tokenizer_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 90
- **Mô tả module**: Tokenizer factory.
- **Imports nổi bật**: collections.abc (Callable), typing (TYPE_CHECKING), graphrag_common.factory (Factory), graphrag_llm.config.types (TokenizerType), graphrag_llm.tokenizer.tokenizer (Tokenizer)
- **Hàm top-level**:
  - `register_tokenizer(tokenizer_type, tokenizer_initializer, scope) -> None`
    - Mục đích: Register a custom tokenizer implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/tokenizer/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_tokenizer(tokenizer_config) -> Tokenizer`
    - Mục đích: Create a Tokenizer instance based on the configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/tokenizer/__init__.py, packages/graphrag-llm/notebooks/02_encoding_decoding.ipynb, packages/graphrag/graphrag/tokenizer/get_tokenizer.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TokenizerFactory`
    - Mục đích: Factory for creating Tokenizer instances.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/types`

- Số file: **2**

#### File: `packages/graphrag-llm/graphrag_llm/types/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 59
- **Mô tả module**: Types module for graphrag-llm.
- **Imports nổi bật**: graphrag_llm.types.types (AsyncLLMCompletionFunction, AsyncLLMEmbeddingFunction, AsyncLLMFunction, LLMChoice, LLMChoiceChunk, LLMChoiceDelta, LLMCompletionArgs, LLMCompletionChunk, LLMCompletionFunction, LLMCompletionFunctionToolParam, LLMCompletionMessage, LLMCompletionMessagesParam, LLMCompletionResponse, LLMCompletionTokensDetails, LLMCompletionUsage, LLMEmbedding, LLMEmbeddingArgs, LLMEmbeddingFunction, LLMEmbeddingResponse, LLMEmbeddingUsage, LLMFunction, LLMPromptTokensDetails, Metrics, ResponseFormat)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/types/types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 266
- **Mô tả module**: Types for graphrag-llm.
- **Imports nổi bật**: collections.abc (AsyncIterator, Awaitable, Iterator, Sequence), typing (Any, Generic, Literal, Protocol, Required, TypeVar, Unpack, runtime_checkable), litellm (AnthropicThinkingParam, ChatCompletionAudioParam, ChatCompletionModality, ChatCompletionPredictionContentParam, OpenAIWebSearchOptions), openai.types.chat.chat_completion (ChatCompletion, Choice), openai.types.chat.chat_completion_chunk (ChatCompletionChunk, ChoiceDelta), openai.types.chat.chat_completion_chunk (Choice), openai.types.chat.chat_completion_function_tool_param (ChatCompletionFunctionToolParam), openai.types.chat.chat_completion_message (ChatCompletionMessage), openai.types.chat.chat_completion_message_param (ChatCompletionMessageParam), openai.types.completion_usage (CompletionTokensDetails, CompletionUsage, PromptTokensDetails), openai.types.create_embedding_response (CreateEmbeddingResponse, Usage), openai.types.embedding (Embedding)
- **Class top-level**:
  - `LLMCompletionResponse`
    - Mục đích: LLM Completion Response extending OpenAI ChatCompletion.
    - Methods chính: content
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/metrics/default_metrics_processor.py
  - `LLMCompletionArgs`
    - Mục đích: Arguments for LLMCompletionFunction.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/threading/completion_thread.py, packages/graphrag-llm/graphrag_llm/threading/completion_thread_runner.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
  - `LLMCompletionFunction`
    - Mục đích: Synchronous completion function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/threading/completion_thread.py, packages/graphrag-llm/graphrag_llm/threading/completion_thread_runner.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
  - `AsyncLLMCompletionFunction`
    - Mục đích: Asynchronous completion function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
  - `LLMEmbeddingResponse`
    - Mục đích: LLM Embedding Response extending OpenAI CreateEmbeddingResponse.
    - Methods chính: embeddings, first_embedding
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/example_notebooks/basic_embedding_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/embedding/mock_llm_embedding.py, packages/graphrag-llm/graphrag_llm/metrics/default_metrics_processor.py
  - `LLMEmbeddingArgs`
    - Mục đích: Arguments for embedding functions.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/embedding/mock_llm_embedding.py, packages/graphrag-llm/graphrag_llm/threading/embedding_thread.py, packages/graphrag-llm/graphrag_llm/threading/embedding_thread_runner.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
  - `LLMEmbeddingFunction`
    - Mục đích: Synchronous embedding function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/threading/embedding_thread.py, packages/graphrag-llm/graphrag_llm/threading/embedding_thread_runner.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
  - `AsyncLLMEmbeddingFunction`
    - Mục đích: Asynchronous embedding function.
    - Methods chính: __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py, packages/graphrag-llm/graphrag_llm/types/__init__.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/graphrag_llm/utils`

- Số file: **7**

#### File: `packages/graphrag-llm/graphrag_llm/utils/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 41
- **Mô tả module**: Utils module.
- **Imports nổi bật**: graphrag_llm.utils.completion_messages_builder (CompletionContentPartBuilder, CompletionMessagesBuilder), graphrag_llm.utils.create_completion_response (create_completion_response), graphrag_llm.utils.create_embedding_response (create_embedding_response), graphrag_llm.utils.function_tool_manager (FunctionArgumentModel, FunctionDefinition, FunctionToolManager, ToolMessage), graphrag_llm.utils.gather_completion_response (gather_completion_response, gather_completion_response_async), graphrag_llm.utils.structure_response (structure_completion_response)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/completion_messages_builder.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 329
- **Mô tả module**: ChatCompletionMessageParamBuilder class.
- **Imports nổi bật**: collections.abc (Iterable), typing (TYPE_CHECKING, Literal), openai.types.chat.chat_completion_assistant_message_param (ChatCompletionAssistantMessageParam), openai.types.chat.chat_completion_content_part_image_param (ChatCompletionContentPartImageParam, ImageURL), openai.types.chat.chat_completion_content_part_input_audio_param (ChatCompletionContentPartInputAudioParam, InputAudio), openai.types.chat.chat_completion_content_part_param (ChatCompletionContentPartParam), openai.types.chat.chat_completion_content_part_text_param (ChatCompletionContentPartTextParam), openai.types.chat.chat_completion_developer_message_param (ChatCompletionDeveloperMessageParam), openai.types.chat.chat_completion_function_message_param (ChatCompletionFunctionMessageParam), openai.types.chat.chat_completion_message (ChatCompletionMessage), openai.types.chat.chat_completion_system_message_param (ChatCompletionSystemMessageParam), openai.types.chat.chat_completion_tool_message_param (ChatCompletionToolMessageParam)
- **Class top-level**:
  - `CompletionMessagesBuilder`
    - Mục đích: CompletionMessagesBuilder class.
    - Methods chính: __init__, add_system_message, add_developer_message, add_tool_message, add_function_message, add_user_message, add_assistant_message, build
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py, packages/graphrag-llm/notebooks/01_basic.ipynb, packages/graphrag-llm/notebooks/09_message_builder_and_history.ipynb, packages/graphrag-llm/notebooks/10_tool_calling.ipynb, packages/graphrag/graphrag/index/operations/extract_covariates/claim_extractor.py, packages/graphrag/graphrag/index/operations/extract_graph/graph_extractor.py
  - `CompletionContentPartBuilder`
    - Mục đích: CompletionContentPartBuilder class.
    - Methods chính: __init__, add_text_part, add_image_part, add_audio_part, build
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py, packages/graphrag-llm/notebooks/09_message_builder_and_history.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/create_completion_response.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 46
- **Mô tả module**: Create completion response.
- **Imports nổi bật**: graphrag_llm.types (LLMChoice, LLMCompletionMessage, LLMCompletionResponse, LLMCompletionUsage)
- **Hàm top-level**:
  - `create_completion_response(response) -> LLMCompletionResponse`
    - Mục đích: Create a completion response object.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/utils/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/create_embedding_response.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 40
- **Mô tả module**: Create embedding response utilities.
- **Imports nổi bật**: graphrag_llm.types (LLMEmbedding, LLMEmbeddingResponse, LLMEmbeddingUsage)
- **Hàm top-level**:
  - `create_embedding_response(embeddings, batch_size) -> LLMEmbeddingResponse`
    - Mục đích: Create a CreateEmbeddingResponse object.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/embedding/mock_llm_embedding.py, packages/graphrag-llm/graphrag_llm/types/types.py, packages/graphrag-llm/graphrag_llm/utils/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/function_tool_manager.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 139
- **Mô tả module**: Function tool manager.
- **Imports nổi bật**: json, collections.abc (Callable), typing (TYPE_CHECKING, Any, Generic, TypeVar), openai (pydantic_function_tool), pydantic (BaseModel), typing_extensions (TypedDict)
- **Class top-level**:
  - `FunctionDefinition`
    - Mục đích: Function definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py
  - `ToolMessage`
    - Mục đích: Function tool response message to be added to message history.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py
  - `FunctionToolManager`
    - Mục đích: Function tool manager.
    - Methods chính: __init__, register_function_tool, definitions, call_functions
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py, packages/graphrag-llm/notebooks/10_tool_calling.ipynb
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/gather_completion_response.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 58
- **Mô tả module**: Gather Completion Response Utility.
- **Imports nổi bật**: collections.abc (AsyncIterator, Iterator), typing (TYPE_CHECKING)
- **Hàm top-level**:
  - `gather_completion_response(response) -> str`
    - Mục đích: Gather completion response from an iterator of response chunks.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/README.md, packages/graphrag-llm/example_notebooks/basic_completion_example.ipynb, packages/graphrag-llm/graphrag_llm/README.md, packages/graphrag-llm/graphrag_llm/utils/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `gather_completion_response_async(response) -> str`
    - Mục đích: Gather completion response from an iterator of response chunks.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/utils/__init__.py, packages/graphrag/graphrag/query/context_builder/rate_relevancy.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/graphrag_llm/utils/structure_response.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 30
- **Mô tả module**: Structure response as pydantic base model.
- **Imports nổi bật**: json, typing (Any, TypeVar), pydantic (BaseModel)
- **Hàm top-level**:
  - `structure_completion_response(response, model) -> T`
    - Mục đích: Structure completion response as pydantic base model.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/completion/mock_llm_completion.py, packages/graphrag-llm/graphrag_llm/utils/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/notebooks`

- Số file: **13**

#### File: `packages/graphrag-llm/notebooks/01_basic.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 16 cells (code=8, markdown=8)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/02_encoding_decoding.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 6 cells (code=3, markdown=3)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/03_structured_responses.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 4 cells (code=2, markdown=2)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/04_metrics.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 13 cells (code=6, markdown=7)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/05_caching.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 8 cells (code=3, markdown=5)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/06_retries.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 2 cells (code=1, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/07_rate_limiting.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=1, markdown=2)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/08_batching.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 18 cells (code=6, markdown=12)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/09_message_builder_and_history.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 6 cells (code=3, markdown=3)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/10_tool_calling.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 8 cells (code=3, markdown=5)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/11_templating.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 2 cells (code=1, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/12_mocking.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 5 cells (code=2, markdown=3)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-llm/notebooks/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 11
- **Heading chính**: # API Key and version are optional, # If not provided, Azure managed identity will be used
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-llm/notebooks/templates`

- Số file: **1**

#### File: `packages/graphrag-llm/notebooks/templates/weather_listings.jinja`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-storage`

- Số file: **2**

#### File: `packages/graphrag-storage/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 44
- **Heading chính**: # GraphRAG Storage, ## Basic, ## Custom Storage, ## Details, # storage_factory has no preregistered providers so you must register any, # providers you plan on using., # May also register a custom implementation, see above for example.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 49
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-storage/example_notebooks`

- Số file: **2**

#### File: `packages/graphrag-storage/example_notebooks/basic_storage_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/example_notebooks/custom_storage_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-storage/graphrag_storage`

- Số file: **10**

#### File: `packages/graphrag-storage/graphrag_storage/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 23
- **Mô tả module**: The GraphRAG Storage package.
- **Imports nổi bật**: graphrag_storage.storage (Storage), graphrag_storage.storage_config (StorageConfig), graphrag_storage.storage_factory (create_storage, register_storage), graphrag_storage.storage_type (StorageType), graphrag_storage.tables (TableProvider)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/azure_blob_storage.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 279
- **Mô tả module**: Azure Blob Storage implementation of Storage.
- **Imports nổi bật**: logging, re, collections.abc (Iterator), pathlib (Path), typing (Any), azure.identity (DefaultAzureCredential), azure.storage.blob (BlobServiceClient), graphrag_storage.storage (Storage, get_timestamp_formatted_with_local_tz)
- **Hàm top-level**:
  - `_validate_blob_container_name(container_name) -> None`
    - Mục đích: Check if the provided blob container name is valid based on Azure rules.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `AzureBlobStorage`
    - Mục đích: The Blob-Storage implementation.
    - Methods chính: __init__, _create_container, _delete_container, _container_exists, find, get, set, has, delete, clear, child, keys
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/README.md, packages/graphrag-storage/graphrag_storage/storage_factory.py, tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_factory.py, tests/smoke/test_fixtures.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/azure_cosmos_storage.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 437
- **Mô tả module**: Azure CosmosDB Storage implementation of PipelineStorage.
- **Imports nổi bật**: json, logging, re, collections.abc (Iterator), datetime (datetime, timezone), io (BytesIO, StringIO), typing (Any), pandas, azure.cosmos (ContainerProxy, CosmosClient, DatabaseProxy), azure.cosmos.exceptions (CosmosResourceNotFoundError), azure.cosmos.partition_key (PartitionKey), azure.identity (DefaultAzureCredential)
- **Hàm top-level**:
  - `_create_progress_status(num_loaded, num_filtered, num_total) -> Progress`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `AzureCosmosStorage`
    - Mục đích: The CosmosDB-Storage Implementation.
    - Methods chính: __init__, _create_database, _delete_database, _create_container, _delete_container, find, get, set, has, _query_all_items, _query_count, delete
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/README.md, packages/graphrag-storage/graphrag_storage/storage_factory.py, tests/integration/storage/test_cosmosdb_storage.py, tests/integration/storage/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/file_storage.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 155
- **Mô tả module**: File-based Storage implementation of Storage.
- **Imports nổi bật**: logging, os, re, shutil, collections.abc (Iterator), datetime (datetime, timezone), pathlib (Path), typing (Any, cast), aiofiles, aiofiles.os (remove), aiofiles.ospath (exists), graphrag_storage.storage (Storage, get_timestamp_formatted_with_local_tz)
- **Hàm top-level**:
  - `_join_path(file_path, file_name) -> Path`
    - Mục đích: Join a path and a file. Independent of the OS.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `FileStorage`
    - Mục đích: File storage class definition.
    - Methods chính: __init__, find, get, _read_file, set, has, delete, clear, child, keys, get_creation_date, get_path
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/README.md, packages/graphrag-storage/graphrag_storage/memory_storage.py, packages/graphrag-storage/graphrag_storage/storage_factory.py, packages/graphrag-storage/graphrag_storage/tables/csv_table.py, packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py, tests/integration/storage/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/memory_storage.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 103
- **Mô tả module**: In-memory storage implementation.
- **Imports nổi bật**: re, collections.abc (Iterator), typing (TYPE_CHECKING, Any), graphrag_storage.file_storage (FileStorage)
- **Class top-level**:
  - `MemoryStorage`
    - Mục đích: In memory storage class definition.
    - Methods chính: __init__, get, set, has, delete, clear, child, keys, find
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/README.md, packages/graphrag-storage/graphrag_storage/storage_factory.py, packages/graphrag/graphrag/index/run/utils.py, tests/integration/storage/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/py.typed`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/storage.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 142
- **Mô tả module**: Abstract base class for storage.
- **Imports nổi bật**: re, abc (ABC, abstractmethod), collections.abc (Iterator), datetime (datetime), typing (Any)
- **Hàm top-level**:
  - `get_timestamp_formatted_with_local_tz(timestamp) -> str`
    - Mục đích: Get the formatted timestamp with the local time zone.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/azure_blob_storage.py, packages/graphrag-storage/graphrag_storage/azure_cosmos_storage.py, packages/graphrag-storage/graphrag_storage/file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `Storage`
    - Mục đích: Provide a storage interface.
    - Methods chính: __init__, find, get, set, has, delete, clear, child, keys, get_creation_date
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/cache.py, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-cache/graphrag_cache/json_cache.py, packages/graphrag-input/graphrag_input/input_reader.py, packages/graphrag-input/graphrag_input/input_reader_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/storage_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 49
- **Mô tả module**: Storage configuration model.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field), graphrag_storage.storage_type (StorageType)
- **Class top-level**:
  - `StorageConfig`
    - Mục đích: The default configuration section for storage.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/cache_config.py, packages/graphrag-cache/graphrag_cache/json_cache.py, packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-storage/README.md
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/storage_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 79
- **Mô tả module**: Storage factory implementation.
- **Imports nổi bật**: collections.abc (Callable), graphrag_common.factory (Factory, ServiceScope), graphrag_storage.storage (Storage), graphrag_storage.storage_config (StorageConfig), graphrag_storage.storage_type (StorageType)
- **Hàm top-level**:
  - `register_storage(storage_type, storage_initializer, scope) -> None`
    - Mục đích: Register a custom storage implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/example_notebooks/custom_storage_example.ipynb, packages/graphrag-storage/graphrag_storage/__init__.py, tests/integration/storage/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_storage(config) -> Storage`
    - Mục đích: Create a storage implementation based on the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-cache/graphrag_cache/json_cache.py, packages/graphrag-input/example_notebooks/input_example.ipynb, packages/graphrag-storage/README.md, packages/graphrag-storage/example_notebooks/basic_storage_example.ipynb, packages/graphrag-storage/example_notebooks/custom_storage_example.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `StorageFactory`
    - Mục đích: A factory class for storage implementations.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/storage_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: Builtin storage implementation types.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `StorageType`
    - Mục đích: Enum for storage types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/cache_config.py, packages/graphrag-llm/notebooks/05_caching.ipynb, packages/graphrag-storage/README.md, packages/graphrag-storage/example_notebooks/basic_storage_example.ipynb, packages/graphrag-storage/graphrag_storage/__init__.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-storage/graphrag_storage/tables`

- Số file: **10**

#### File: `packages/graphrag-storage/graphrag_storage/tables/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 10
- **Mô tả module**: Table provider module for GraphRAG storage.
- **Imports nổi bật**: table (Table), table_provider (TableProvider)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/csv_table.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 204
- **Mô tả module**: A CSV-based implementation of the Table abstraction for streaming row access.
- **Imports nổi bật**: __future__ (annotations), csv, inspect, os, shutil, sys, tempfile, pathlib (Path), typing (TYPE_CHECKING, Any), aiofiles, graphrag_storage.file_storage (FileStorage), graphrag_storage.tables.table (RowTransformer, Table)
- **Hàm top-level**:
  - `_identity(row) -> Any`
    - Mục đích: Return row unchanged (default transformer).
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/parquet_table.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_apply_transformer(transformer, row) -> Any`
    - Mục đích: Apply transformer to row, handling both callables and classes.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/parquet_table.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `CSVTable`
    - Mục đích: Row-by-row streaming interface for CSV tables.
    - Methods chính: __init__, __aiter__, _aiter_impl, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table.py, packages/graphrag/graphrag/data_model/row_transformers.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py, tests/unit/indexing/test_create_communities.py, tests/unit/indexing/test_finalize_graph.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 141
- **Mô tả module**: CSV-based table provider implementation.
- **Imports nổi bật**: logging, re, io (StringIO), pandas, graphrag_storage.file_storage (FileStorage), graphrag_storage.storage (Storage), graphrag_storage.tables.csv_table (CSVTable), graphrag_storage.tables.table (RowTransformer), graphrag_storage.tables.table_provider (TableProvider)
- **Class top-level**:
  - `CSVTableProvider`
    - Mục đích: Table provider that stores tables as CSV files using an underlying Storage instance.
    - Methods chính: __init__, read_dataframe, write_dataframe, has, list, open
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py, tests/unit/storage/test_csv_table_provider.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/parquet_table.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 151
- **Mô tả module**: A Parquet-based implementation of the Table abstraction with simulated streaming.
- **Imports nổi bật**: __future__ (annotations), inspect, io (BytesIO), typing (TYPE_CHECKING, Any, cast), pandas, graphrag_storage.tables.table (RowTransformer, Table)
- **Hàm top-level**:
  - `_identity(row) -> Any`
    - Mục đích: Return row unchanged (default transformer).
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/csv_table.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_apply_transformer(transformer, row) -> Any`
    - Mục đích: Apply transformer to row, handling both callables and classes.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/csv_table.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ParquetTable`
    - Mục đích: Simulated streaming interface for Parquet tables.
    - Methods chính: __init__, __aiter__, _aiter_impl, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/parquet_table_provider.py, packages/graphrag/graphrag/data_model/row_transformers.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/parquet_table_provider.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 139
- **Mô tả module**: Parquet-based table provider implementation.
- **Imports nổi bật**: logging, re, io (BytesIO), pandas, graphrag_storage.storage (Storage), graphrag_storage.tables.parquet_table (ParquetTable), graphrag_storage.tables.table (RowTransformer, Table), graphrag_storage.tables.table_provider (TableProvider)
- **Class top-level**:
  - `ParquetTableProvider`
    - Mục đích: Table provider that stores tables as Parquet files using an underlying Storage instance.
    - Methods chính: __init__, read_dataframe, write_dataframe, has, list, open
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py, packages/graphrag/graphrag/index/run/utils.py, tests/unit/storage/test_parquet_table_provider.py, tests/verbs/test_create_final_text_units.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/table.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 126
- **Mô tả module**: Table abstraction for streaming row-by-row access.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (AsyncIterator, Callable), types (TracebackType), typing (Any), typing_extensions (Self)
- **Class top-level**:
  - `Table`
    - Mục đích: Abstract base class for streaming table access.
    - Methods chính: __aiter__, length, has, write, close, __aenter__, __aexit__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/__init__.py, packages/graphrag-storage/graphrag_storage/tables/csv_table.py, packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/table_provider.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/table_provider.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 103
- **Mô tả module**: Abstract base class for table providers.
- **Imports nổi bật**: abc (ABC, abstractmethod), typing (Any), pandas, graphrag_storage.tables.table (RowTransformer, Table)
- **Class top-level**:
  - `TableProvider`
    - Mục đích: Provide a table-based storage interface with support for DataFrames and row dictionaries.
    - Methods chính: __init__, read_dataframe, write_dataframe, has, list, open
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/__init__.py, packages/graphrag-storage/graphrag_storage/tables/__init__.py, packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py, packages/graphrag/graphrag/data_model/data_reader.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/table_provider_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 21
- **Mô tả module**: Storage configuration model.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field), graphrag_storage.tables.table_type (TableType)
- **Class top-level**:
  - `TableProviderConfig`
    - Mục đích: The default configuration section for table providers.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py, packages/graphrag/graphrag/config/models/graph_rag_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 83
- **Mô tả module**: Storage factory implementation.
- **Imports nổi bật**: collections.abc (Callable), graphrag_common.factory (Factory, ServiceScope), graphrag_storage.storage (Storage), graphrag_storage.tables.table_provider (TableProvider), graphrag_storage.tables.table_provider_config (TableProviderConfig), graphrag_storage.tables.table_type (TableType)
- **Hàm top-level**:
  - `register_table_provider(table_type, table_initializer, scope) -> None`
    - Mục đích: Register a custom storage implementation.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_table_provider(config, storage) -> TableProvider`
    - Mục đích: Create a table provider implementation based on the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/index/run/run_pipeline.py, packages/graphrag/graphrag/index/run/utils.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TableProviderFactory`
    - Mục đích: A factory class for table storage implementations.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-storage/graphrag_storage/tables/table_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 15
- **Mô tả module**: Builtin table storage implementation types.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `TableType`
    - Mục đích: Enum for table storage types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table_provider_config.py, packages/graphrag-storage/graphrag_storage/tables/table_provider_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-vectors`

- Số file: **2**

#### File: `packages/graphrag-vectors/README.md`
- **Loại**: markdown
- **Vai trò**: Tài liệu hướng dẫn sử dụng/tham chiếu nhanh cho thư mục hoặc package.
- **Số dòng**: 34
- **Heading chính**: # GraphRAG Vectors, ## Basic usage with the utility function (recommended), ## Basic usage implementing the factory directly, ## Supported Vector Stores, ## Custom Vector Store, ## Configuration
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/pyproject.toml`
- **Loại**: config/data
- **Vai trò**: Khai báo package, dependencies, build system và metadata phát hành.
- **Số dòng**: 50
- **Key cấu hình chính**: name, version, description, authors, license, readme, requires-python, classifiers, dependencies, Source, requires, build-backend
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-vectors/example_notebooks`

- Số file: **7**

#### File: `packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 13 cells (code=8, markdown=5)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/basic_usage_factory_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/basic_usage_with_utility_function_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 13 cells (code=8, markdown=5)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 3 cells (code=2, markdown=1)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 22 cells (code=12, markdown=10)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/lancedb.ipynb`
- **Loại**: notebook
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Notebook**: 13 cells (code=8, markdown=5)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-vectors/example_notebooks/data`

- Số file: **2**

#### File: `packages/graphrag-vectors/example_notebooks/data/embeddings.text_unit_text.parquet`
- **Loại**: other
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/example_notebooks/data/text_units.parquet`
- **Loại**: other
- **Vai trò**: Notebook ví dụ/minh họa cách dùng package hoặc kiểm thử tương tác.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag-vectors/graphrag_vectors`

- Số file: **12**

#### File: `packages/graphrag-vectors/graphrag_vectors/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 53
- **Mô tả module**: GraphRAG vector store implementations.
- **Imports nổi bật**: graphrag_vectors.filtering (AndExpr, Condition, F, FilterExpr, NotExpr, Operator, OrExpr), graphrag_vectors.index_schema (IndexSchema), graphrag_vectors.timestamp (explode_timestamp), graphrag_vectors.types (TextEmbedder), graphrag_vectors.vector_store (VectorStore, VectorStoreDocument, VectorStoreSearchResult), graphrag_vectors.vector_store_config (VectorStoreConfig), graphrag_vectors.vector_store_factory (VectorStoreFactory, create_vector_store, register_vector_store, vector_store_factory), graphrag_vectors.vector_store_type (VectorStoreType)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 374
- **Mô tả module**: A package containing the Azure AI Search  vector store implementation.
- **Imports nổi bật**: typing (Any), azure.core.credentials (AzureKeyCredential), azure.identity (DefaultAzureCredential), azure.search.documents (SearchClient), azure.search.documents.indexes (SearchIndexClient), azure.search.documents.indexes.models (HnswAlgorithmConfiguration, HnswParameters, SearchField, SearchFieldDataType, SearchIndex, SimpleField, VectorSearch, VectorSearchAlgorithmMetric, VectorSearchProfile), azure.search.documents.models (VectorizedQuery), graphrag_vectors.filtering (AndExpr, Condition, FilterExpr, NotExpr, Operator, OrExpr), graphrag_vectors.vector_store (VectorStore, VectorStoreDocument, VectorStoreSearchResult)
- **Class top-level**:
  - `AzureAISearchVectorStore`
    - Mục đích: Azure AI Search vector storage implementation.
    - Methods chính: __init__, connect, create_index, load_documents, _compile_filter, _compile_condition, _extract_data, similarity_search_by_vector, search_by_id, count, remove, update
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb, packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py, tests/integration/vector_stores/test_azure_ai_search.py, tests/integration/vector_stores/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/cosmosdb.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 422
- **Mô tả module**: A package containing the CosmosDB vector store implementation.
- **Imports nổi bật**: typing (Any), azure.cosmos (ContainerProxy, CosmosClient, DatabaseProxy), azure.cosmos.exceptions (CosmosHttpResponseError), azure.cosmos.partition_key (PartitionKey), azure.identity (DefaultAzureCredential), graphrag_vectors.filtering (AndExpr, Condition, FilterExpr, NotExpr, Operator, OrExpr), graphrag_vectors.vector_store (VectorStore, VectorStoreDocument, VectorStoreSearchResult)
- **Class top-level**:
  - `CosmosDBVectorStore`
    - Mục đích: Azure CosmosDB vector storage implementation.
    - Methods chính: __init__, connect, _create_database, _delete_database, _database_exists, _create_container, _delete_container, _container_exists, create_index, load_documents, _compile_filter, _compile_condition
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb, packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py, tests/integration/vector_stores/test_cosmosdb.py, tests/integration/vector_stores/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/filtering.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 387
- **Mô tả module**: Generic filter expressions for vector store queries.
- **Imports nổi bật**: __future__ (annotations), enum (StrEnum), typing (Annotated, Any), pydantic (BaseModel, ConfigDict, Field)
- **Hàm top-level**:
  - `_make_and(left, right) -> AndExpr`
    - Mục đích: Create AND expression, flattening nested ANDs.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_or(left, right) -> OrExpr`
    - Mục đích: Create OR expression, flattening nested ORs.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `Operator`
    - Mục đích: Comparison operators for filter conditions.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py, tests/unit/vector_stores/test_filtering.py
  - `Condition`
    - Mục đích: A single filter condition comparing a field to a value.
    - Methods chính: evaluate, _get_field_value, _compare, __and__, __or__, __invert__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/notebooks/03_structured_responses.ipynb, packages/graphrag-llm/notebooks/11_templating.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py
  - `AndExpr`
    - Mục đích: Logical AND of multiple filter expressions.
    - Methods chính: evaluate, __and__, __or__, __invert__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py, tests/unit/vector_stores/test_filtering.py
  - `OrExpr`
    - Mục đích: Logical OR of multiple filter expressions.
    - Methods chính: evaluate, __and__, __or__, __invert__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py, tests/unit/vector_stores/test_filtering.py
  - `NotExpr`
    - Mục đích: Logical NOT of a filter expression.
    - Methods chính: evaluate, __and__, __or__, __invert__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py, tests/unit/vector_stores/test_filtering.py
  - `FieldRef`
    - Mục đích: Reference to a field for building filter expressions with a fluent API.
    - Methods chính: __init__, __eq__, __ne__, __gt__, __ge__, __lt__, __le__, contains, startswith, endswith, in_, not_in
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `_FieldBuilder`
    - Mục đích: Builder for creating field references via attribute access.
    - Methods chính: __getattr__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/index_schema.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 62
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: re, pydantic (BaseModel, Field, model_validator)
- **Hàm top-level**:
  - `is_valid_field_name(field) -> bool`
    - Mục đích: Check if a field name is valid for CosmosDB.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `IndexSchema`
    - Mục đích: The default configuration section for Vector Store Schema.
    - Methods chính: _validate_schema, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/README.md, packages/graphrag-vectors/example_notebooks/basic_usage_factory_example.ipynb, packages/graphrag-vectors/example_notebooks/basic_usage_with_utility_function_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/lancedb.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 273
- **Mô tả module**: The LanceDB vector storage implementation package.
- **Imports nổi bật**: typing (Any), lancedb, numpy, pyarrow, graphrag_vectors.filtering (AndExpr, Condition, FilterExpr, NotExpr, Operator, OrExpr), graphrag_vectors.vector_store (VectorStore, VectorStoreDocument, VectorStoreSearchResult)
- **Class top-level**:
  - `LanceDBVectorStore`
    - Mục đích: LanceDB vector storage implementation.
    - Methods chính: __init__, connect, create_index, load_documents, _extract_data, _compile_filter, _compile_condition, similarity_search_by_vector, search_by_id, count, remove, update
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/basic_usage_factory_example.ipynb, packages/graphrag-vectors/example_notebooks/lancedb.ipynb, packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py, tests/integration/vector_stores/test_factory.py, tests/integration/vector_stores/test_lancedb.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/timestamp.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 96
- **Mô tả module**: Timestamp explosion for vector store indexing.
- **Imports nổi bật**: datetime (datetime)
- **Hàm top-level**:
  - `_timestamp_fields_for(prefix) -> dict[str, str]`
    - Mục đích: Return the exploded field definitions for a given prefix.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/vector_store.py, tests/unit/vector_stores/test_timestamp.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `explode_timestamp(iso_timestamp, prefix) -> dict[str, str | int]`
    - Mục đích: Explode an ISO 8601 timestamp into filterable component fields.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/vector_store.py, tests/unit/vector_stores/test_timestamp.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: Common types for vector stores.
- **Imports nổi bật**: collections.abc (Callable)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/vector_store.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 217
- **Mô tả module**: Base classes for vector stores.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (Callable), dataclasses (dataclass, field), datetime (datetime, timezone), typing (Any), graphrag_vectors.filtering (FilterExpr), graphrag_vectors.timestamp (TIMESTAMP_FIELDS, _timestamp_fields_for, explode_timestamp), graphrag_vectors.types (TextEmbedder)
- **Class top-level**:
  - `VectorStoreDocument`
    - Mục đích: A document that is stored in vector storage.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb, packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/example_notebooks/lancedb.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py
  - `VectorStoreSearchResult`
    - Mục đích: A vector storage search result.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py, tests/unit/query/context_builder/test_entity_extraction.py
  - `VectorStore`
    - Mục đích: The base class for vector storage data-access classes.
    - Methods chính: __init__, _now_iso, _prepare_document, _prepare_update, connect, create_index, load_documents, insert, similarity_search_by_vector, similarity_search_by_text, search_by_id, count
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py, packages/graphrag-vectors/graphrag_vectors/lancedb.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/vector_store_config.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 59
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field), graphrag_vectors.index_schema (DEFAULT_VECTOR_SIZE, IndexSchema), graphrag_vectors.vector_store_type (VectorStoreType)
- **Class top-level**:
  - `VectorStoreConfig`
    - Mục đích: The default configuration section for Vector Store.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/README.md, packages/graphrag-vectors/example_notebooks/basic_usage_with_utility_function_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 100
- **Mô tả module**: Factory functions for creating a vector store.
- **Imports nổi bật**: __future__ (annotations), typing (TYPE_CHECKING), graphrag_common.factory (Factory, ServiceScope), graphrag_vectors.vector_store (VectorStore), graphrag_vectors.vector_store_type (VectorStoreType)
- **Hàm top-level**:
  - `register_vector_store(vector_store_type, vector_store_initializer, scope) -> None`
    - Mục đích: Register a custom vector store implementation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_vector_store(config, index_schema) -> VectorStore`
    - Mục đích: Create a vector store implementation based on the given type and configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/README.md, packages/graphrag-vectors/example_notebooks/basic_usage_with_utility_function_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_example.ipynb, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag/graphrag/index/workflows/generate_text_embeddings.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `VectorStoreFactory`
    - Mục đích: A factory for vector stores.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, tests/integration/vector_stores/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag-vectors/graphrag_vectors/vector_store_type.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 15
- **Mô tả module**: Vector store type enum.
- **Imports nổi bật**: enum (StrEnum)
- **Class top-level**:
  - `VectorStoreType`
    - Mục đích: The supported vector store types.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/basic_usage_factory_example.ipynb, packages/graphrag-vectors/graphrag_vectors/__init__.py, packages/graphrag-vectors/graphrag_vectors/vector_store_config.py, packages/graphrag-vectors/graphrag_vectors/vector_store_factory.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/graph_rag_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag`

- Số file: **3**

#### File: `packages/graphrag/graphrag/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: The GraphRAG package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/__main__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: The GraphRAG package.
- **Imports nổi bật**: graphrag.cli.main (app)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/py.typed`
- **Loại**: other
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/api`

- Số file: **4**

#### File: `packages/graphrag/graphrag/api/__init__.py`
- **Loại**: python
- **Vai trò**: Lớp API public để ứng dụng bên ngoài gọi vào GraphRAG.
- **Số dòng**: 40
- **Mô tả module**: API for GraphRAG.
- **Imports nổi bật**: graphrag.api.index (build_index), graphrag.api.prompt_tune (generate_indexing_prompts), graphrag.api.query (basic_search, basic_search_streaming, drift_search, drift_search_streaming, global_search, global_search_streaming, local_search, local_search_streaming), graphrag.prompt_tune.types (DocSelectionType)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/api/index.py`
- **Loại**: python
- **Vai trò**: Lớp API public để ứng dụng bên ngoài gọi vào GraphRAG.
- **Số dòng**: 99
- **Mô tả module**: Indexing API for GraphRAG.
- **Imports nổi bật**: logging, typing (Any), pandas, graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (IndexingMethod), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.run.run_pipeline (run_pipeline), graphrag.index.run.utils (create_callback_chain), graphrag.index.typing.pipeline_run_result (PipelineRunResult), graphrag.index.workflows.factory (PipelineFactory), graphrag.logger.standard_logging (init_loggers)
- **Hàm top-level**:
  - `build_index(config, method, is_update_run, callbacks, additional_context, verbose, input_documents) -> list[PipelineRunResult]`
    - Mục đích: Run the pipeline with the given configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/index.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_method(method, is_update_run) -> str`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/api/prompt_tune.py`
- **Loại**: python
- **Vai trò**: Lớp API public để ứng dụng bên ngoài gọi vào GraphRAG.
- **Số dòng**: 187
- **Mô tả module**: Auto Templating API.
- **Imports nổi bật**: logging, graphrag_llm.completion (create_completion), pydantic (PositiveInt, validate_call), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.logger.standard_logging (init_loggers), graphrag.prompt_tune.defaults (MAX_TOKEN_COUNT, PROMPT_TUNING_MODEL_ID), graphrag.prompt_tune.generator.community_report_rating (generate_community_report_rating), graphrag.prompt_tune.generator.community_report_summarization (create_community_summarization_prompt), graphrag.prompt_tune.generator.community_reporter_role (generate_community_reporter_role), graphrag.prompt_tune.generator.domain (generate_domain), graphrag.prompt_tune.generator.entity_relationship (generate_entity_relationship_examples), graphrag.prompt_tune.generator.entity_summarization_prompt (create_entity_summarization_prompt)
- **Hàm top-level**:
  - `generate_indexing_prompts(config, limit, selection_method, domain, language, max_tokens, discover_entity_types, min_examples_required, n_subset_max, k, verbose) -> tuple[str, str, str]`
    - Mục đích: Generate indexing prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/api/query.py`
- **Loại**: python
- **Vai trò**: Lớp API public để ứng dụng bên ngoài gọi vào GraphRAG.
- **Số dòng**: 547
- **Mô tả module**: Query Engine API.
- **Imports nổi bật**: logging, collections.abc (AsyncGenerator), typing (Any), pandas, pydantic (validate_call), graphrag.callbacks.noop_query_callbacks (NoopQueryCallbacks), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.config.embeddings (community_full_content_embedding, entity_description_embedding, text_unit_text_embedding), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.logger.standard_logging (init_loggers), graphrag.query.factory (get_basic_search_engine, get_drift_search_engine, get_global_search_engine, get_local_search_engine), graphrag.query.indexer_adapters (read_indexer_communities, read_indexer_covariates, read_indexer_entities, read_indexer_relationships, read_indexer_report_embeddings, read_indexer_reports, read_indexer_text_units)
- **Hàm top-level**:
  - `global_search(config, entities, communities, community_reports, community_level, dynamic_community_selection, response_type, query, callbacks, verbose) -> tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]`
    - Mục đích: Perform a global search and return the context data and response.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/global_search_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `global_search_streaming(config, entities, communities, community_reports, community_level, dynamic_community_selection, response_type, query, callbacks, verbose) -> AsyncGenerator`
    - Mục đích: Perform a global search and return the context data and response via a generator.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `local_search(config, entities, communities, community_reports, text_units, relationships, covariates, community_level, response_type, query, callbacks, verbose) -> tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]`
    - Mục đích: Perform a local search and return the context data and response.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/config/models/local_search_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `local_search_streaming(config, entities, communities, community_reports, text_units, relationships, covariates, community_level, response_type, query, callbacks, verbose) -> AsyncGenerator`
    - Mục đích: Perform a local search and return the context data and response via a generator.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `drift_search(config, entities, communities, community_reports, text_units, relationships, community_level, response_type, query, callbacks, verbose) -> tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]`
    - Mục đích: Perform a DRIFT search and return the context data and response.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/drift_search_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `drift_search_streaming(config, entities, communities, community_reports, text_units, relationships, community_level, response_type, query, callbacks, verbose) -> AsyncGenerator`
    - Mục đích: Perform a DRIFT search and return the context data and response.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `basic_search(config, text_units, response_type, query, callbacks, verbose) -> tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]`
    - Mục đích: Perform a basic search and return the context data and response.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/basic_search_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `basic_search_streaming(config, text_units, response_type, query, callbacks, verbose) -> AsyncGenerator`
    - Mục đích: Perform a local search and return the context data and response via a generator.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/cli/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/cache`

- Số file: **2**

#### File: `packages/graphrag/graphrag/cache/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Cache module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cache/cache_key_creator.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 45
- **Mô tả module**: Cache key creation for Graphrag.
- **Imports nổi bật**: typing (Any), graphrag_llm.cache (create_cache_key)
- **Hàm top-level**:
  - `cache_key_creator(input_args) -> str`
    - Mục đích: Generate a cache key based on input arguments.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/completion/completion.py, packages/graphrag-llm/graphrag_llm/completion/completion_factory.py, packages/graphrag-llm/graphrag_llm/completion/lite_llm_completion.py, packages/graphrag-llm/graphrag_llm/embedding/embedding.py, packages/graphrag-llm/graphrag_llm/embedding/embedding_factory.py, packages/graphrag-llm/graphrag_llm/embedding/lite_llm_embedding.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/callbacks`

- Số file: **8**

#### File: `packages/graphrag/graphrag/callbacks/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: A package containing callback implementations.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/console_workflow_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 51
- **Mô tả module**: A logger that emits updates from the indexing engine to the console.
- **Imports nổi bật**: graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.index.typing.pipeline_run_result (PipelineRunResult), graphrag.logger.progress (Progress)
- **Class top-level**:
  - `ConsoleWorkflowCallbacks`
    - Mục đích: A logger that writes to a console.
    - Methods chính: __init__, pipeline_start, pipeline_end, workflow_start, workflow_end, pipeline_error, progress
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/index.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/llm_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 15
- **Mô tả module**: LLM Callbacks.
- **Imports nổi bật**: typing (Protocol)
- **Class top-level**:
  - `BaseLLMCallback`
    - Mục đích: Base class for LLM callbacks.
    - Methods chính: on_llm_new_token
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/callbacks/query_callbacks.py, packages/graphrag/graphrag/query/question_gen/local_gen.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/noop_query_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 34
- **Mô tả module**: No-op Query Callbacks.
- **Imports nổi bật**: typing (Any), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.query.structured_search.base (SearchResult)
- **Class top-level**:
  - `NoopQueryCallbacks`
    - Mục đích: A no-op implementation of QueryCallbacks.
    - Methods chính: on_context, on_map_response_start, on_map_response_end, on_reduce_response_start, on_reduce_response_end, on_llm_new_token
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py, packages/graphrag/graphrag/cli/query.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/noop_workflow_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 31
- **Mô tả module**: A no-op implementation of WorkflowCallbacks.
- **Imports nổi bật**: graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.typing.pipeline_run_result (PipelineRunResult), graphrag.logger.progress (Progress)
- **Class top-level**:
  - `NoopWorkflowCallbacks`
    - Mục đích: A no-op implementation of WorkflowCallbacks that logs all events to standard logging.
    - Methods chính: pipeline_start, pipeline_end, workflow_start, workflow_end, progress, pipeline_error
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/callbacks/console_workflow_callbacks.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, packages/graphrag/graphrag/index/run/utils.py, packages/graphrag/graphrag/index/utils/derive_from_rows.py, packages/graphrag/graphrag/prompt_tune/loader/input.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/query_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 34
- **Mô tả module**: Query Callbacks.
- **Imports nổi bật**: typing (Any), graphrag.callbacks.llm_callbacks (BaseLLMCallback), graphrag.query.structured_search.base (SearchResult)
- **Class top-level**:
  - `QueryCallbacks`
    - Mục đích: Callbacks used during query execution.
    - Methods chính: on_context, on_map_response_start, on_map_response_end, on_reduce_response_start, on_reduce_response_end, on_llm_new_token
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py, packages/graphrag/graphrag/callbacks/noop_query_callbacks.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/basic_search/search.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/workflow_callbacks.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 42
- **Mô tả module**: Collection of callbacks that can be used to monitor the workflow execution.
- **Imports nổi bật**: typing (Protocol), graphrag.index.typing.pipeline_run_result (PipelineRunResult), graphrag.logger.progress (Progress)
- **Class top-level**:
  - `WorkflowCallbacks`
    - Mục đích: A collection of callbacks that can be used to monitor the workflow execution.
    - Methods chính: pipeline_start, pipeline_end, workflow_start, workflow_end, progress, pipeline_error
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/callbacks/noop_workflow_callbacks.py, packages/graphrag/graphrag/callbacks/workflow_callbacks_manager.py, packages/graphrag/graphrag/index/operations/embed_text/embed_text.py, packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py, packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/callbacks/workflow_callbacks_manager.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 59
- **Mô tả module**: A module containing 'WorkflowCallbacksManager' model.
- **Imports nổi bật**: graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.typing.pipeline_run_result (PipelineRunResult), graphrag.logger.progress (Progress)
- **Class top-level**:
  - `WorkflowCallbacksManager`
    - Mục đích: A registry of WorkflowCallbacks.
    - Methods chính: __init__, register, pipeline_start, pipeline_end, workflow_start, workflow_end, progress, pipeline_error
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/cli`

- Số file: **6**

#### File: `packages/graphrag/graphrag/cli/__init__.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 5
- **Mô tả module**: CLI for GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cli/index.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 136
- **Mô tả module**: CLI implementation of the index subcommand.
- **Imports nổi bật**: asyncio, logging, sys, warnings, pathlib (Path), graphrag_cache.cache_type (CacheType), graphrag.api, graphrag.callbacks.console_workflow_callbacks (ConsoleWorkflowCallbacks), graphrag.config.enums (IndexingMethod), graphrag.config.load_config (load_config), graphrag.index.validate_config (validate_config_names), graphrag.utils.cli (redact)
- **Hàm top-level**:
  - `_register_signal_handlers()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `index_cli(root_dir, method, verbose, cache, dry_run, skip_validation)`
    - Mục đích: Run the pipeline with the given config.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `update_cli(root_dir, method, verbose, cache, skip_validation)`
    - Mục đích: Run the pipeline with the given config.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_run_index(config, method, is_update_run, verbose, cache, dry_run, skip_validation)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cli/initialize.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 102
- **Mô tả module**: CLI implementation of the initialization subcommand.
- **Imports nổi bật**: logging, pathlib (Path), graphrag.config.defaults (graphrag_config_defaults), graphrag.config.init_content (INIT_DOTENV, INIT_YAML), graphrag.prompts.index.community_report (COMMUNITY_REPORT_PROMPT), graphrag.prompts.index.community_report_text_units (COMMUNITY_REPORT_TEXT_PROMPT), graphrag.prompts.index.extract_claims (EXTRACT_CLAIMS_PROMPT), graphrag.prompts.index.extract_graph (GRAPH_EXTRACTION_PROMPT), graphrag.prompts.index.summarize_descriptions (SUMMARIZE_PROMPT), graphrag.prompts.query.basic_search_system_prompt (BASIC_SEARCH_SYSTEM_PROMPT), graphrag.prompts.query.drift_search_system_prompt (DRIFT_LOCAL_SYSTEM_PROMPT, DRIFT_REDUCE_PROMPT), graphrag.prompts.query.global_search_knowledge_system_prompt (GENERAL_KNOWLEDGE_INSTRUCTION)
- **Hàm top-level**:
  - `initialize_project_at(path, force, model, embedding_model) -> None`
    - Mục đích: Initialize the project at the given path.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cli/main.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 482
- **Mô tả module**: CLI entrypoint.
- **Imports nổi bật**: os, re, collections.abc (Callable), pathlib (Path), typer, graphrag.config.defaults (DEFAULT_COMPLETION_MODEL, DEFAULT_EMBEDDING_MODEL, graphrag_config_defaults), graphrag.config.enums (IndexingMethod, SearchMethod), graphrag.prompt_tune.defaults (LIMIT, MAX_TOKEN_COUNT, N_SUBSET_MAX, K), graphrag.prompt_tune.types (DocSelectionType)
- **Hàm top-level**:
  - `path_autocomplete(file_okay, dir_okay, readable, writable, match_wildcard) -> Callable[[str], list[str]]`
    - Mục đích: Autocomplete file and directory paths.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_initialize_cli(root, model, embedding_model, force) -> None`
    - Mục đích: Generate a default configuration file.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_index_cli(root, method, verbose, dry_run, cache, skip_validation) -> None`
    - Mục đích: Build a knowledge graph index.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_cli(root, method, verbose, cache, skip_validation) -> None`
    - Mục đích: Update an existing knowledge graph index.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prompt_tune_cli(root, verbose, domain, selection_method, n_subset_max, k, limit, max_tokens, min_examples_required, chunk_size, overlap, language, discover_entity_types, output) -> None`
    - Mục đích: Generate custom graphrag prompts with your own data (i.e. auto templating).
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_query_cli(query, root, method, verbose, data, community_level, dynamic_community_selection, response_type, streaming) -> None`
    - Mục đích: Query a knowledge graph index.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cli/prompt_tune.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 115
- **Mô tả module**: CLI implementation of the prompt-tune subcommand.
- **Imports nổi bật**: logging, pathlib (Path), graphrag.api, graphrag.config.load_config (load_config), graphrag.prompt_tune.generator.community_report_summarization (COMMUNITY_SUMMARIZATION_FILENAME), graphrag.prompt_tune.generator.entity_summarization_prompt (ENTITY_SUMMARIZATION_FILENAME), graphrag.prompt_tune.generator.extract_graph_prompt (EXTRACT_GRAPH_FILENAME), graphrag.utils.cli (redact)
- **Hàm top-level**:
  - `prompt_tune(root, domain, verbose, selection_method, limit, max_tokens, chunk_size, overlap, language, discover_entity_types, output, n_subset_max, k, min_examples_required)`
    - Mục đích: Prompt tune the model.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/cli/main.py, packages/graphrag/graphrag/prompt_tune/generator/community_report_rating.py, packages/graphrag/graphrag/prompt_tune/generator/community_report_summarization.py, packages/graphrag/graphrag/prompt_tune/generator/community_reporter_role.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/cli/query.py`
- **Loại**: python
- **Vai trò**: Lệnh CLI: parse argument và điều phối workflow.
- **Số dòng**: 398
- **Mô tả module**: CLI implementation of the query subcommand.
- **Imports nổi bật**: asyncio, sys, pathlib (Path), typing (TYPE_CHECKING, Any), graphrag_storage (create_storage), graphrag_storage.tables.table_provider_factory (create_table_provider), graphrag.api, graphrag.callbacks.noop_query_callbacks (NoopQueryCallbacks), graphrag.config.load_config (load_config), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader)
- **Hàm top-level**:
  - `run_global_search(data_dir, root_dir, community_level, dynamic_community_selection, response_type, streaming, query, verbose)`
    - Mục đích: Perform a global search with a given query.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_local_search(data_dir, root_dir, community_level, response_type, streaming, query, verbose)`
    - Mục đích: Perform a local search with a given query.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_drift_search(data_dir, root_dir, community_level, response_type, streaming, query, verbose)`
    - Mục đích: Perform a local search with a given query.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_basic_search(data_dir, root_dir, response_type, streaming, query, verbose)`
    - Mục đích: Perform a basics search with a given query.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_resolve_output_files(config, output_list, optional_list) -> dict[str, Any]`
    - Mục đích: Read indexing output files to a dataframe dict, with correct column types.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/config`

- Số file: **7**

#### File: `packages/graphrag/graphrag/config/__init__.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 5
- **Mô tả module**: The config package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/defaults.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 386
- **Mô tả module**: Common default configuration values.
- **Imports nổi bật**: dataclasses (dataclass, field), pathlib (Path), typing (ClassVar), graphrag_cache (CacheType), graphrag_chunking.chunk_strategy_type (ChunkerType), graphrag_input (InputType), graphrag_llm.config (AuthMethod), graphrag_storage (StorageType), graphrag_vectors (VectorStoreType), graphrag.config.embeddings (default_embeddings), graphrag.config.enums (AsyncType, NounPhraseExtractorType, ReportingType), graphrag.index.operations.build_noun_graph.np_extractors.stop_words (EN_STOP_WORDS)
- **Class top-level**:
  - `BasicSearchDefaults`
    - Mục đích: Default values for basic search.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ChunkingDefaults`
    - Mục đích: Default values for chunking.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ClusterGraphDefaults`
    - Mục đích: Default values for cluster graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `CommunityReportDefaults`
    - Mục đích: Default values for community report.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `DriftSearchDefaults`
    - Mục đích: Default values for drift search.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `EmbedTextDefaults`
    - Mục đích: Default values for embedding text.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ExtractClaimsDefaults`
    - Mục đích: Default values for claim extraction.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ExtractGraphDefaults`
    - Mục đích: Default values for extracting graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TextAnalyzerDefaults`
    - Mục đích: Default values for text analyzer.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ExtractGraphNLPDefaults`
    - Mục đích: Default values for NLP graph extraction.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `GlobalSearchDefaults`
    - Mục đích: Default values for global search.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `StorageDefaults`
    - Mục đích: Default values for storage.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `InputDefaults`
    - Mục đích: Default values for input.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `InputStorageDefaults`
    - Mục đích: Default values for input storage.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `CacheStorageDefaults`
    - Mục đích: Default values for cache storage.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `CacheDefaults`
    - Mục đích: Default values for cache.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `LocalSearchDefaults`
    - Mục đích: Default values for local search.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `OutputStorageDefaults`
    - Mục đích: Default values for output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `PruneGraphDefaults`
    - Mục đích: Default values for pruning graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ReportingDefaults`
    - Mục đích: Default values for reporting.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/embeddings.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 20
- **Mô tả module**: A module containing embeddings values.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/enums.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 78
- **Mô tả module**: A module containing config enums.
- **Imports nổi bật**: __future__ (annotations), enum (Enum)
- **Class top-level**:
  - `ReportingType`
    - Mục đích: The reporting configuration type for the pipeline.
    - Methods chính: __repr__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/config/models/reporting_config.py, packages/graphrag/graphrag/logger/factory.py, tests/integration/logging/test_factory.py
  - `AsyncType`
    - Mục đích: Enum for the type of async to use.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/extract_graph_nlp_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py, packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py
  - `SearchMethod`
    - Mục đích: The type of search to run.
    - Methods chính: __str__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/main.py
  - `IndexingMethod`
    - Mục đích: Enum for the type of indexing to perform.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/cli/index.py, packages/graphrag/graphrag/cli/main.py, packages/graphrag/graphrag/index/workflows/factory.py
  - `NounPhraseExtractorType`
    - Mục đích: Enum for the noun phrase extractor options.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/extract_graph_nlp_config.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py
  - `ModularityMetric`
    - Mục đích: Enum for the modularity metric to use.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/errors.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 42
- **Mô tả module**: Errors for the default configuration.
- **Class top-level**:
  - `ApiKeyMissingError`
    - Mục đích: LLM Key missing error.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `AzureApiBaseMissingError`
    - Mục đích: Azure API Base missing error.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `AzureApiVersionMissingError`
    - Mục đích: Azure API version missing error.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ConflictingSettingsError`
    - Mục đích: Missing model configuration error.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/init_content.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 145
- **Mô tả module**: Content for the init CLI command to generate a default configuration.
- **Imports nổi bật**: graphrag.config.defaults, graphrag.config.defaults (graphrag_config_defaults, vector_store_defaults)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/load_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 48
- **Mô tả module**: Default method for loading config.
- **Imports nổi bật**: pathlib (Path), typing (Any), graphrag_common.config (load_config), graphrag.config.models.graph_rag_config (GraphRagConfig)
- **Hàm top-level**:
  - `load_config(root_dir, cli_overrides) -> GraphRagConfig`
    - Mục đích: Load configuration from a file.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-common/README.md, packages/graphrag-common/example_notebooks/config_module_example.ipynb, packages/graphrag-common/graphrag_common/config/__init__.py, packages/graphrag-common/graphrag_common/config/load_config.py, packages/graphrag/graphrag/cli/index.py, packages/graphrag/graphrag/cli/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/config/models`

- Số file: **16**

#### File: `packages/graphrag/graphrag/config/models/__init__.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 5
- **Mô tả module**: Interfaces for Default Config parameterization.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/basic_search_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 34
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `BasicSearchConfig`
    - Mục đích: The default configuration section for Cache.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/cluster_graph_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 26
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `ClusterGraphConfig`
    - Mục đích: Configuration section for clustering graphs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/community_reports_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 64
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: dataclasses (dataclass), pathlib (Path), pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.prompts.index.community_report (COMMUNITY_REPORT_PROMPT), graphrag.prompts.index.community_report_text_units (COMMUNITY_REPORT_TEXT_PROMPT)
- **Class top-level**:
  - `CommunityReportPrompts`
    - Mục đích: Community report prompt templates.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `CommunityReportsConfig`
    - Mục đích: Configuration section for community reports.
    - Methods chính: resolved_prompts
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/drift_search_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 124
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `DRIFTSearchConfig`
    - Mục đích: The default configuration section for Cache.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py, packages/graphrag/graphrag/query/structured_search/drift_search/primer.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/embed_text_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 34
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `EmbedTextConfig`
    - Mục đích: Configuration section for text embeddings.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/extract_claims_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 57
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: dataclasses (dataclass), pathlib (Path), pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.prompts.index.extract_claims (EXTRACT_CLAIMS_PROMPT)
- **Class top-level**:
  - `ClaimExtractionPrompts`
    - Mục đích: Claim extraction prompt templates.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ExtractClaimsConfig`
    - Mục đích: Configuration section for claim extraction.
    - Methods chính: resolved_prompts
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/extract_graph_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 53
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: dataclasses (dataclass), pathlib (Path), pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.prompts.index.extract_graph (GRAPH_EXTRACTION_PROMPT)
- **Class top-level**:
  - `ExtractGraphPrompts`
    - Mục đích: Graph extraction prompt templates.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ExtractGraphConfig`
    - Mục đích: Configuration section for entity extraction.
    - Methods chính: resolved_prompts
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/extract_graph_nlp_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 75
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.config.enums (AsyncType, NounPhraseExtractorType)
- **Class top-level**:
  - `TextAnalyzerConfig`
    - Mục đích: Configuration section for NLP text analyzer.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py, tests/unit/config/utils.py
  - `ExtractGraphNLPConfig`
    - Mục đích: Configuration section for graph extraction via NLP.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/global_search_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 68
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `GlobalSearchConfig`
    - Mục đích: The default configuration section for Cache.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/graph_rag_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 334
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: dataclasses (asdict), pathlib (Path), devtools (pformat), graphrag_cache (CacheConfig), graphrag_chunking.chunking_config (ChunkingConfig), graphrag_input (InputConfig), graphrag_llm.config (ModelConfig), graphrag_storage (StorageConfig, StorageType), graphrag_storage.tables.table_provider_config (TableProviderConfig), graphrag_vectors (IndexSchema, VectorStoreConfig, VectorStoreType), pydantic (BaseModel, Field, model_validator), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `GraphRagConfig`
    - Mục đích: Base class for the Default-Configuration parameterization settings.
    - Methods chính: __repr__, __str__, _validate_input_base_dir, _validate_output_base_dir, _validate_update_output_storage_base_dir, _validate_reporting_base_dir, _validate_vector_store, _validate_vector_store_db_uri, get_completion_model_config, get_embedding_model_config, _validate_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/api/query.py, packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/config/load_config.py, packages/graphrag/graphrag/index/run/run_pipeline.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/local_search_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 50
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `LocalSearchConfig`
    - Mục đích: The default configuration section for Cache.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/prune_graph_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 42
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `PruneGraphConfig`
    - Mục đích: Configuration section for pruning graphs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/index/workflows/prune_graph.py, tests/unit/config/utils.py, tests/verbs/test_prune_graph.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/reporting_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 35
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.config.enums (ReportingType)
- **Class top-level**:
  - `ReportingConfig`
    - Mục đích: The default configuration section for Reporting.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/snapshots_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 26
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults)
- **Class top-level**:
  - `SnapshotsConfig`
    - Mục đích: Configuration section for snapshots.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/config/models/summarize_descriptions_config.py`
- **Loại**: python
- **Vai trò**: Định nghĩa schema/config, default, validation và nạp cấu hình.
- **Số dòng**: 53
- **Mô tả module**: Parameterization settings for the default configuration.
- **Imports nổi bật**: dataclasses (dataclass), pathlib (Path), pydantic (BaseModel, Field), graphrag.config.defaults (graphrag_config_defaults), graphrag.prompts.index.summarize_descriptions (SUMMARIZE_PROMPT)
- **Class top-level**:
  - `SummarizeDescriptionsPrompts`
    - Mục đích: Description summarization prompt templates.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `SummarizeDescriptionsConfig`
    - Mục đích: Configuration section for description summarization.
    - Methods chính: resolved_prompts
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/graph_rag_config.py, tests/unit/config/utils.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/data_model`

- Số file: **15**

#### File: `packages/graphrag/graphrag/data_model/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: Knowledge model package.
- **Imports nổi bật**: graphrag.data_model.data_reader (DataReader)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/community.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 80
- **Mô tả module**: A package containing the 'Community' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.named (Named)
- **Class top-level**:
  - `Community`
    - Mục đích: A protocol for a community in the system.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/models/community_reports_config.py, packages/graphrag/graphrag/index/operations/summarize_communities/__init__.py, packages/graphrag/graphrag/index/operations/summarize_communities/community_reports_extractor.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/typing.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/community_report.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 68
- **Mô tả module**: A package containing the 'CommunityReport' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.named (Named)
- **Class top-level**:
  - `CommunityReport`
    - Mục đích: Defines an LLM-generated summary report of a community.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, packages/graphrag/graphrag/index/operations/summarize_communities/typing.py, packages/graphrag/graphrag/query/context_builder/community_context.py, packages/graphrag/graphrag/query/context_builder/dynamic_community_selection.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/covariate.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 55
- **Mô tả module**: A package containing the 'Covariate' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.identified (Identified)
- **Class top-level**:
  - `Covariate`
    - Mục đích: A protocol for a covariate in the system.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py, packages/graphrag/graphrag/index/operations/extract_covariates/typing.py, packages/graphrag/graphrag/query/context_builder/local_context.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py, packages/graphrag/graphrag/query/input/loaders/dfs.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/data_reader.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 72
- **Mô tả module**: A DataReader that loads typed dataframes from a TableProvider.
- **Imports nổi bật**: pandas, graphrag_storage.tables (TableProvider), graphrag.data_model.dfs (communities_typed, community_reports_typed, covariates_typed, documents_typed, entities_typed, relationships_typed, text_units_typed)
- **Class top-level**:
  - `DataReader`
    - Mục đích: Reads dataframes from a TableProvider and applies correct column types.
    - Methods chính: __init__, entities, relationships, communities, community_reports, covariates, text_units, documents
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/query.py, packages/graphrag/graphrag/data_model/__init__.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/extract_covariates.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/dfs.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 153
- **Mô tả module**: A package containing dataframe processing utilities.
- **Imports nổi bật**: typing (Any), pandas, graphrag.data_model.schemas (COMMUNITY_CHILDREN, COMMUNITY_ID, COMMUNITY_LEVEL, COVARIATE_IDS, EDGE_DEGREE, EDGE_WEIGHT, ENTITY_IDS, FINDINGS, N_TOKENS, NODE_DEGREE, NODE_FREQUENCY, PERIOD, RATING, RELATIONSHIP_IDS, SHORT_ID, SIZE, TEXT_UNIT_IDS)
- **Hàm top-level**:
  - `_safe_int(series, fill) -> pd.Series`
    - Mục đích: Convert a series to int, filling NaN values first.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `split_list_column(value) -> list[Any]`
    - Mục đích: Split a column containing a list string into an actual list.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `entities_typed(df) -> pd.DataFrame`
    - Mục đích: Return the entities dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `relationships_typed(df) -> pd.DataFrame`
    - Mục đích: Return the relationships dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `communities_typed(df) -> pd.DataFrame`
    - Mục đích: Return the communities dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `community_reports_typed(df) -> pd.DataFrame`
    - Mục đích: Return the community reports dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `covariates_typed(df) -> pd.DataFrame`
    - Mục đích: Return the covariates dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `text_units_typed(df) -> pd.DataFrame`
    - Mục đích: Return the text units dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `documents_typed(df) -> pd.DataFrame`
    - Mục đích: Return the documents dataframe with correct types, in case it was stored in a weakly-typed format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/data_reader.py, packages/graphrag/graphrag/data_model/row_transformers.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/document.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 50
- **Mô tả module**: A package containing the 'Document' model.
- **Imports nổi bật**: dataclasses (dataclass, field), typing (Any), graphrag.data_model.named (Named)
- **Class top-level**:
  - `Document`
    - Mục đích: A protocol for a document in the system.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb, packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb, packages/graphrag-vectors/example_notebooks/lancedb.ipynb, packages/graphrag-vectors/graphrag_vectors/lancedb.py, packages/graphrag-vectors/graphrag_vectors/vector_store.py, packages/graphrag/graphrag/api/query.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/entity.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 70
- **Mô tả module**: A package containing the 'Entity' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.named (Named)
- **Class top-level**:
  - `Entity`
    - Mục đích: A protocol for an entity in the system.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table.py, packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py, packages/graphrag/graphrag/index/operations/prune_graph.py, packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py, packages/graphrag/graphrag/index/operations/summarize_descriptions/typing.py, packages/graphrag/graphrag/index/update/entities.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/identified.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 18
- **Mô tả module**: A package containing the 'Identified' protocol.
- **Imports nổi bật**: dataclasses (dataclass)
- **Class top-level**:
  - `Identified`
    - Mục đích: A protocol for an item with an ID.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/covariate.py, packages/graphrag/graphrag/data_model/named.py, packages/graphrag/graphrag/data_model/relationship.py, packages/graphrag/graphrag/data_model/text_unit.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/named.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 17
- **Mô tả module**: A package containing the 'Named' protocol.
- **Imports nổi bật**: dataclasses (dataclass), graphrag.data_model.identified (Identified)
- **Class top-level**:
  - `Named`
    - Mục đích: A protocol for an item with a name/title.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/community.py, packages/graphrag/graphrag/data_model/community_report.py, packages/graphrag/graphrag/data_model/document.py, packages/graphrag/graphrag/data_model/entity.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/relationship.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 66
- **Mô tả module**: A package containing the 'Relationship' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.identified (Identified)
- **Class top-level**:
  - `Relationship`
    - Mục đích: A relationship between two entities. This is a generic relationship, and can be used to represent any type of relationship between any two entities.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/update/relationships.py, packages/graphrag/graphrag/query/context_builder/entity_extraction.py, packages/graphrag/graphrag/query/context_builder/local_context.py, packages/graphrag/graphrag/query/context_builder/source_context.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/row_transformers.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 253
- **Mô tả module**: Row-level type coercion for streaming Table reads.
- **Imports nổi bật**: typing (Any), graphrag.data_model.dfs (split_list_column)
- **Hàm top-level**:
  - `_safe_int(value, fill) -> int`
    - Mục đích: Coerce a value to int, returning *fill* when missing or empty.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_safe_float(value, fill) -> float`
    - Mục đích: Coerce a value to float, returning *fill* when missing or empty.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_coerce_list(value) -> list[Any]`
    - Mục đích: Parse a value into a list, handling CSV string and array types.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_entity_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for an entity row.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_final_text_units.py, packages/graphrag/graphrag/index/workflows/finalize_graph.py, tests/verbs/test_create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_entity_row_for_embedding(row) -> dict[str, Any]`
    - Mục đích: Add a title_description column for embedding generation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/generate_text_embeddings.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_relationship_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a relationship row.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_final_text_units.py, packages/graphrag/graphrag/index/workflows/finalize_graph.py, tests/verbs/test_create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_community_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a community row.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_community_report_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a community report row.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_covariate_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a covariate row.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_text_unit_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a text-unit row.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_final_text_units.py, tests/verbs/test_create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_document_row(row) -> dict[str, Any]`
    - Mục đích: Coerce types for a document row.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/schemas.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 160
- **Mô tả module**: Common field name definitions for data frames.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/text_unit.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 63
- **Mô tả module**: A package containing the 'TextUnit' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.data_model.identified (Identified)
- **Class top-level**:
  - `TextUnit`
    - Mục đích: A protocol for a TextUnit item in a Document database.
    - Methods chính: from_dict
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/source_context.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py, packages/graphrag/graphrag/query/input/loaders/dfs.py, packages/graphrag/graphrag/query/input/retrieval/text_units.py, packages/graphrag/graphrag/query/structured_search/basic_search/basic_context.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/data_model/types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 9
- **Mô tả module**: Common types for the GraphRAG knowledge model.
- **Imports nổi bật**: collections.abc (Callable)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/graphs`

- Số file: **7**

#### File: `packages/graphrag/graphrag/graphs/__init__.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 5
- **Mô tả module**: Graph utilities that operate on DataFrames instead of NetworkX objects.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/compute_degree.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 44
- **Mô tả module**: Compute node degree directly from a relationships DataFrame.
- **Imports nổi bật**: pandas
- **Hàm top-level**:
  - `compute_degree(relationships, source_column, target_column) -> pd.DataFrame`
    - Mục đích: Compute the degree of each node from an edge list DataFrame.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/prune_graph.py, packages/graphrag/graphrag/index/workflows/finalize_graph.py, tests/unit/graphs/test_compute_degree.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/connected_components.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 94
- **Mô tả module**: Find connected components and the largest connected component from an edge list DataFrame.
- **Imports nổi bật**: pandas
- **Hàm top-level**:
  - `connected_components(relationships, source_column, target_column) -> list[set[str]]`
    - Mục đích: Return all connected components as a list of node-title sets.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py, packages/graphrag/graphrag/graphs/stable_lcc.py, packages/graphrag/graphrag/index/operations/prune_graph.py, tests/unit/graphs/nx_stable_lcc.py, tests/unit/graphs/test_connected_components.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `largest_connected_component(relationships, source_column, target_column) -> set[str]`
    - Mục đích: Return the node titles belonging to the largest connected component.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py, packages/graphrag/graphrag/graphs/stable_lcc.py, packages/graphrag/graphrag/index/operations/prune_graph.py, tests/unit/graphs/test_connected_components.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/edge_weights.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 102
- **Mô tả module**: Edge weight calculation utilities (PMI, RRF).
- **Imports nổi bật**: numpy, pandas
- **Hàm top-level**:
  - `calculate_pmi_edge_weights(nodes_df, edges_df, node_name_col, node_freq_col, edge_weight_col, edge_source_col, edge_target_col) -> pd.DataFrame`
    - Mục đích: Calculate pointwise mutual information (PMI) edge weights.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/build_noun_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_rrf_edge_weights(nodes_df, edges_df, node_name_col, node_freq_col, edge_weight_col, edge_source_col, edge_target_col, rrf_smoothing_factor) -> pd.DataFrame`
    - Mục đích: Calculate reciprocal rank fusion (RRF) edge weights.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/hierarchical_leiden.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 55
- **Mô tả module**: Hierarchical Leiden clustering on edge lists.
- **Imports nổi bật**: typing (Any), graspologic_native
- **Hàm top-level**:
  - `hierarchical_leiden(edges, max_cluster_size, random_seed) -> list[gn.HierarchicalCluster]`
    - Mục đích: Run hierarchical leiden on an edge list.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py, packages/graphrag/graphrag/index/operations/cluster_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `first_level_hierarchical_clustering(hcs) -> dict[Any, int]`
    - Mục đích: Return the initial leiden clustering as a dict of node id to community id.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `final_level_hierarchical_clustering(hcs) -> dict[Any, int]`
    - Mục đích: Return the final leiden clustering as a dict of node id to community id.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/modularity.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 296
- **Mô tả module**: Compute graph modularity directly from an edge list DataFrame.
- **Imports nổi bật**: logging, math, collections (defaultdict), pandas, graphrag.config.enums (ModularityMetric), graphrag.graphs.connected_components (connected_components, largest_connected_component), graphrag.graphs.hierarchical_leiden (final_level_hierarchical_clustering, first_level_hierarchical_clustering, hierarchical_leiden)
- **Hàm top-level**:
  - `_df_to_edge_list(edges, source_column, target_column, weight_column) -> list[tuple[str, str, float]]`
    - Mục đích: Convert a relationships DataFrame to a sorted edge list.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `modularity(edges, partitions, source_column, target_column, weight_column, resolution) -> float`
    - Mục đích: Calculate modularity of a graph given community assignments.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/enums.py, tests/unit/graphs/test_modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_modularity_component(intra_community_degree, total_community_degree, network_degree_sum, resolution) -> float`
    - Mục đích: Compute the modularity contribution of a single community.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_modularity_components(edges, partitions, source_column, target_column, weight_column, resolution) -> dict[int, float]`
    - Mục đích: Calculate per-community modularity components from an edge list.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_root_modularity(edges, max_cluster_size, random_seed) -> float`
    - Mục đích: Calculate modularity of the graph's root clusters.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_leaf_modularity(edges, max_cluster_size, random_seed) -> float`
    - Mục đích: Calculate modularity of the graph's leaf clusters.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_graph_modularity(edges, max_cluster_size, random_seed, use_root_modularity) -> float`
    - Mục đích: Calculate modularity of the whole graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_lcc_modularity(edges, max_cluster_size, random_seed, use_root_modularity) -> float`
    - Mục đích: Calculate modularity of the largest connected component of the graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_weighted_modularity(edges, max_cluster_size, random_seed, min_connected_component_size, use_root_modularity) -> float`
    - Mục đích: Calculate weighted modularity of components larger than *min_connected_component_size*.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `calculate_modularity(edges, max_cluster_size, random_seed, use_root_modularity, modularity_metric) -> float`
    - Mục đích: Calculate modularity of the graph based on the modularity metric type.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/graphs/stable_lcc.py`
- **Loại**: python
- **Vai trò**: Xử lý cấu trúc đồ thị, cộng đồng, thuật toán liên quan graph.
- **Số dòng**: 76
- **Mô tả module**: Produce a stable largest connected component from a relationships DataFrame.
- **Imports nổi bật**: html, pandas, graphrag.graphs.connected_components (largest_connected_component)
- **Hàm top-level**:
  - `stable_lcc(relationships, source_column, target_column) -> pd.DataFrame`
    - Mục đích: Return the relationships DataFrame filtered to a stable largest connected component.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/cluster_graph.py, tests/unit/graphs/nx_stable_lcc.py, tests/unit/graphs/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_normalize_name(name) -> str`
    - Mục đích: Normalize a node name: HTML unescape, uppercase, strip whitespace.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index`

- Số file: **2**

#### File: `packages/graphrag/graphrag/index/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The indexing engine package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/validate_config.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 42
- **Mô tả module**: A module containing validate_config_names definition.
- **Imports nổi bật**: asyncio, logging, sys, graphrag_llm.completion (create_completion), graphrag_llm.embedding (create_embedding), graphrag.config.models.graph_rag_config (GraphRagConfig)
- **Hàm top-level**:
  - `validate_config_names(parameters) -> None`
    - Mục đích: Validate config file for model deployment name typos, by running a quick test message for each.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/index.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations`

- Số file: **8**

#### File: `packages/graphrag/graphrag/index/operations/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Reusable data frame operations.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/cluster_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 100
- **Mô tả module**: A module containing cluster_graph method definition.
- **Imports nổi bật**: logging, collections (defaultdict), pandas, graphrag.graphs.hierarchical_leiden (hierarchical_leiden), graphrag.graphs.stable_lcc (stable_lcc)
- **Hàm top-level**:
  - `cluster_graph(edges, max_cluster_size, use_lcc, seed) -> Communities`
    - Mục đích: Apply a hierarchical clustering algorithm to a relationships DataFrame.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/cluster_graph_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/index/workflows/create_communities.py, tests/unit/config/utils.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_compute_leiden_communities(edges, max_cluster_size, use_lcc, seed) -> tuple[dict[int, dict[str, int]], dict[int, int]]`
    - Mục đích: Return Leiden root communities and their hierarchy mapping.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_cluster_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/compute_edge_combined_degree.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 44
- **Mô tả module**: A module containing compute_edge_combined_degree method definition.
- **Imports nổi bật**: typing (cast), pandas
- **Hàm top-level**:
  - `compute_edge_combined_degree(edge_df, node_degree_df, node_name_column, node_degree_column, edge_source_column, edge_target_column) -> pd.Series`
    - Mục đích: Compute the combined degree for each edge in a graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_degree_colname(column) -> str`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/finalize_community_reports.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 35
- **Mô tả module**: All the steps to transform final entities.
- **Imports nổi bật**: pandas, graphrag.data_model.schemas (COMMUNITY_REPORTS_FINAL_COLUMNS), graphrag.index.utils.hashing (gen_sha512_hash)
- **Hàm top-level**:
  - `finalize_community_reports(reports, communities) -> pd.DataFrame`
    - Mục đích: All the steps to transform final community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/finalize_entities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 57
- **Mô tả module**: Stream-finalize entity rows into an output Table.
- **Imports nổi bật**: typing (Any), uuid (uuid4), graphrag_storage.tables.table (Table), graphrag.data_model.schemas (ENTITIES_FINAL_COLUMNS)
- **Hàm top-level**:
  - `finalize_entities(entities_table, degree_map) -> list[dict[str, Any]]`
    - Mục đích: Read entity rows, enrich with degree, and write back.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/finalize_graph.py, tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/finalize_relationships.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 56
- **Mô tả module**: Stream-finalize relationship rows into an output Table.
- **Imports nổi bật**: typing (Any), uuid (uuid4), graphrag_storage.tables.table (Table), graphrag.data_model.schemas (RELATIONSHIPS_FINAL_COLUMNS)
- **Hàm top-level**:
  - `finalize_relationships(relationships_table, degree_map) -> list[dict[str, Any]]`
    - Mục đích: Deduplicate relationships, enrich with combined degree, and write.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/finalize_graph.py, tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/prune_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 116
- **Mô tả module**: Graph pruning.
- **Imports nổi bật**: numpy, pandas, graphrag.data_model.schemas, graphrag.graphs.compute_degree (compute_degree), graphrag.graphs.connected_components (largest_connected_component)
- **Hàm top-level**:
  - `prune_graph(entities, relationships, min_node_freq, max_node_freq_std, min_node_degree, max_node_degree_std, min_edge_weight_pct, remove_ego_nodes, lcc_only) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Prune graph by removing out-of-range nodes and low-weight edges.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/config/models/prune_graph_config.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, packages/graphrag/graphrag/index/workflows/prune_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_upper_threshold_by_std(data, std_trim) -> float`
    - Mục đích: Get upper threshold by standard deviation.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/snapshot_graphml.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 20
- **Mô tả module**: A module containing snapshot_graphml method definition.
- **Imports nổi bật**: networkx, pandas, graphrag_storage (Storage)
- **Hàm top-level**:
  - `snapshot_graphml(edges, name, storage) -> None`
    - Mục đích: Take a entire snapshot of a graph to standard graphml format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/build_noun_graph`

- Số file: **2**

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The Indexing Engine noun graph package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/build_noun_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 144
- **Mô tả module**: Graph extraction using NLP.
- **Imports nổi bật**: logging, collections (defaultdict), itertools (combinations), pandas, graphrag_cache (Cache), graphrag_storage.tables.table (Table), graphrag.graphs.edge_weights (calculate_pmi_edge_weights), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.utils.hashing (gen_sha512_hash)
- **Hàm top-level**:
  - `build_noun_graph(text_unit_table, text_analyzer, normalize_edge_weights, cache) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Build a noun graph from text units.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py, packages/graphrag/graphrag/index/workflows/extract_graph_nlp.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_extract_nodes(text_unit_table, text_analyzer, cache) -> dict[str, list[str]]`
    - Mục đích: Extract noun-phrase nodes from text units.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_extract_edges(title_to_ids, nodes_df, normalize_edge_weights) -> pd.DataFrame`
    - Mục đích: Build co-occurrence edges between noun phrases.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors`

- Số file: **9**

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: NLP-based graph extractors.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/base.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 62
- **Mô tả module**: Base class for noun phrase extractors.
- **Imports nổi bật**: logging, abc (ABCMeta, abstractmethod), spacy
- **Class top-level**:
  - `BaseNounPhraseExtractor`
    - Mục đích: Abstract base class for noun phrase extractors.
    - Methods chính: __init__, extract, __str__, load_spacy_model
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/build_noun_graph.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py, packages/graphrag/graphrag/index/workflows/extract_graph_nlp.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 183
- **Mô tả module**: CFG-based noun phrase extractor.
- **Imports nổi bật**: typing (Any), spacy.tokens.doc (Doc), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.np_validator (has_valid_token_length, is_compound, is_valid_entity)
- **Class top-level**:
  - `CFGNounPhraseExtractor`
    - Mục đích: CFG-based noun phrase extractor.
    - Methods chính: __init__, extract, extract_cfg_matches, _tag_noun_phrases, __str__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 83
- **Mô tả module**: Create a noun phrase extractor from a configuration.
- **Imports nổi bật**: typing (ClassVar), graphrag.config.enums (NounPhraseExtractorType), graphrag.config.models.extract_graph_nlp_config (TextAnalyzerConfig), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.cfg_extractor (CFGNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.regex_extractor (RegexENNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.stop_words (EN_STOP_WORDS), graphrag.index.operations.build_noun_graph.np_extractors.syntactic_parsing_extractor (SyntacticNounPhraseExtractor)
- **Hàm top-level**:
  - `create_noun_phrase_extractor(analyzer_config) -> BaseNounPhraseExtractor`
    - Mục đích: Create a noun phrase extractor from a configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/extract_graph_nlp.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `NounPhraseExtractorFactory`
    - Mục đích: A factory class for creating noun phrase extractor.
    - Methods chính: register, get_np_extractor
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 26
- **Mô tả module**: Util functions to tag noun phrases for filtering.
- **Hàm top-level**:
  - `is_compound(tokens) -> bool`
    - Mục đích: List of tokens forms a compound noun phrase.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `has_valid_token_length(tokens, max_length) -> bool`
    - Mục đích: Check if all tokens have valid length.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `is_valid_entity(entity, tokens) -> bool`
    - Mục đích: Check if the entity is valid.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py, packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 125
- **Mô tả module**: Functions to analyze text data using SpaCy.
- **Imports nổi bật**: re, typing (Any), nltk, textblob (TextBlob), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.resource_loader (download_if_not_exists)
- **Class top-level**:
  - `RegexENNounPhraseExtractor`
    - Mục đích: Regular expression-based noun phrase extractor for English.
    - Methods chính: __init__, extract, _tag_noun_phrases, __str__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/resource_loader.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 39
- **Mô tả module**: Util functions needed for nltk-based noun-phrase extractors (i.e. TextBlob).
- **Imports nổi bật**: nltk
- **Hàm top-level**:
  - `download_if_not_exists(resource_name) -> bool`
    - Mục đích: Download nltk resources if they haven't been already.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/stop_words.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 22
- **Mô tả module**: Custom list of stop words to be excluded by noun phrase extractors.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 163
- **Mô tả module**: Noun phrase extractor based on dependency parsing and NER using SpaCy.
- **Imports nổi bật**: typing (Any), spacy.tokens.span (Span), spacy.util (filter_spans), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.np_validator (has_valid_token_length, is_compound, is_valid_entity)
- **Class top-level**:
  - `SyntacticNounPhraseExtractor`
    - Mục đích: Noun phrase extractor based on dependency parsing and NER using SpaCy.
    - Methods chính: __init__, extract, _tag_noun_phrases, __str__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/embed_text`

- Số file: **3**

#### File: `packages/graphrag/graphrag/index/operations/embed_text/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The Indexing Engine text embed package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/embed_text/embed_text.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 154
- **Mô tả module**: Streaming text embedding operation.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING, Any), numpy, graphrag_llm.tokenizer (Tokenizer), graphrag_storage.tables.table (Table), graphrag_vectors (VectorStore, VectorStoreDocument), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.operations.embed_text.run_embed_text (run_embed_text)
- **Hàm top-level**:
  - `embed_text(input_table, callbacks, model, tokenizer, embed_column, batch_size, batch_max_tokens, num_threads, vector_store, id_column, output_table) -> int`
    - Mục đích: Embed text from a streaming Table into a vector store.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/embed_text_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/index/workflows/generate_text_embeddings.py, packages/graphrag/graphrag/index/workflows/update_text_embeddings.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_flush_embedding_buffer(buffer, embed_column, id_column, callbacks, model, tokenizer, batch_size, batch_max_tokens, num_threads, vector_store, output_table) -> int`
    - Mục đích: Embed a buffer of rows and load results into the vector store.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 171
- **Mô tả module**: A module containing 'TextEmbeddingResult' model and run_embed_text method definition.
- **Imports nổi bật**: asyncio, logging, dataclasses (dataclass), typing (TYPE_CHECKING), numpy, graphrag_chunking.token_chunker (split_text_on_tokens), graphrag_llm.tokenizer (Tokenizer), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.utils.is_null (is_null), graphrag.logger.progress (ProgressTicker, progress_ticker)
- **Hàm top-level**:
  - `run_embed_text(input, callbacks, model, tokenizer, batch_size, batch_max_tokens, num_threads) -> TextEmbeddingResult`
    - Mục đích: Run the Claim extraction chain.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/embed_text/embed_text.py, packages/graphrag/graphrag/prompt_tune/loader/input.py, tests/unit/indexing/operations/embed_text/test_embed_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_execute(model, chunks, tick, semaphore) -> list[list[float]]`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_create_text_batches(texts, tokenizer, max_batch_size, max_batch_tokens) -> list[list[str]]`
    - Mục đích: Create batches of texts to embed.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prepare_embed_texts(input, tokenizer, batch_max_tokens, chunk_overlap) -> tuple[list[str], list[int]]`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_reconstitute_embeddings(raw_embeddings, sizes) -> list[list[float] | None]`
    - Mục đích: Reconstitute the embeddings into the original input texts.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TextEmbeddingResult`
    - Mục đích: Text embedding result class definition.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/operations/embed_text/test_embed_text.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/extract_covariates`

- Số file: **4**

#### File: `packages/graphrag/graphrag/index/operations/extract_covariates/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The Indexing Engine text extract claims package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_covariates/claim_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 194
- **Mô tả module**: A module containing 'ClaimExtractorResult' and 'ClaimExtractor' models.
- **Imports nổi bật**: logging, traceback, dataclasses (dataclass), typing (TYPE_CHECKING, Any), graphrag_llm.utils (CompletionMessagesBuilder), graphrag.config.defaults (graphrag_config_defaults), graphrag.index.typing.error_handler (ErrorHandlerFn), graphrag.prompts.index.extract_claims (CONTINUE_PROMPT, LOOP_PROMPT)
- **Class top-level**:
  - `ClaimExtractorResult`
    - Mục đích: Claim extractor result class definition.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ClaimExtractor`
    - Mục đích: Claim extractor class definition.
    - Methods chính: __init__, __call__, _clean_claim, _process_document, _parse_claim_tuples
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 122
- **Mô tả module**: A module containing the extract_covariates verb definition.
- **Imports nổi bật**: logging, collections.abc (Iterable), dataclasses (asdict), typing (TYPE_CHECKING, Any), pandas, graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.index.operations.extract_covariates.claim_extractor (ClaimExtractor), graphrag.index.operations.extract_covariates.typing (Covariate, CovariateExtractionResult), graphrag.index.utils.derive_from_rows (derive_from_rows)
- **Hàm top-level**:
  - `extract_covariates(input, callbacks, model, column, covariate_type, max_gleanings, claim_description, prompt, entity_types, num_threads, async_type)`
    - Mục đích: Extract claims from a piece of text.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/extract_covariates.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/verbs/test_extract_covariates.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_row_from_claim_data(row, covariate_data, covariate_type)`
    - Mục đích: Create a row from the claim data and the input row.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_extract_claims(input, entity_types, resolved_entities_map, model, max_gleanings, claim_description, prompt) -> CovariateExtractionResult`
    - Mục đích: Run the Claim extraction chain.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_covariate(item) -> Covariate`
    - Mục đích: Create a covariate from the item.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_covariates/typing.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 51
- **Mô tả module**: A module containing 'Covariate' and 'CovariateExtractionResult' models.
- **Imports nổi bật**: collections.abc (Awaitable, Callable, Iterable), dataclasses (dataclass), typing (Any), graphrag_cache (Cache), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks)
- **Class top-level**:
  - `Covariate`
    - Mục đích: Covariate class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/covariate.py, packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py, packages/graphrag/graphrag/query/context_builder/local_context.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py, packages/graphrag/graphrag/query/input/loaders/dfs.py
  - `CovariateExtractionResult`
    - Mục đích: Covariate extraction result class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/extract_graph`

- Số file: **4**

#### File: `packages/graphrag/graphrag/index/operations/extract_graph/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The Indexing Engine entities extraction package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 130
- **Mô tả module**: A module containing extract_graph method.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING), pandas, graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.index.operations.extract_graph.graph_extractor (GraphExtractor), graphrag.index.operations.extract_graph.utils (filter_orphan_relationships), graphrag.index.utils.derive_from_rows (derive_from_rows)
- **Hàm top-level**:
  - `extract_graph(text_units, callbacks, text_column, id_column, model, prompt, entity_types, max_gleanings, num_threads, async_type) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Extract a graph from a piece of text using a language model.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/azure_cosmos_storage.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/cli/initialize.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/extract_graph_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_run_extract_graph(text, source_id, entity_types, model, prompt, max_gleanings) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Run the graph intelligence entity extraction strategy.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_merge_entities(entity_dfs) -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/operations/test_extract_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_merge_relationships(relationship_dfs) -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/operations/test_extract_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_graph/graph_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 189
- **Mô tả module**: Graph extraction helpers that return tabular data.
- **Imports nổi bật**: logging, re, traceback, typing (TYPE_CHECKING, Any), pandas, graphrag_llm.utils (CompletionMessagesBuilder), graphrag.index.typing.error_handler (ErrorHandlerFn), graphrag.index.utils.string (clean_str), graphrag.prompts.index.extract_graph (CONTINUE_PROMPT, LOOP_PROMPT)
- **Hàm top-level**:
  - `_empty_entities_df() -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_empty_relationships_df() -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `GraphExtractor`
    - Mục đích: Unipartite graph extractor class definition.
    - Methods chính: __init__, __call__, _process_document, _process_result
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/extract_graph/utils.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 54
- **Mô tả module**: Utility functions for graph extraction operations.
- **Imports nổi bật**: logging, pandas
- **Hàm top-level**:
  - `filter_orphan_relationships(relationships, entities) -> pd.DataFrame`
    - Mục đích: Remove relationships whose source or target has no entity entry.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py, packages/graphrag/graphrag/index/workflows/update_entities_relationships.py, tests/unit/indexing/operations/test_extract_graph.py, tests/unit/indexing/update/test_update_relationships.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/summarize_communities`

- Số file: **7**

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Community summarization modules.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/build_mixed_context.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 75
- **Mô tả module**: A module containing build_mixed_context method definition.
- **Imports nổi bật**: pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas, graphrag.index.operations.summarize_communities.graph_context.sort_context (sort_context)
- **Hàm top-level**:
  - `build_mixed_context(context, tokenizer, max_context_tokens) -> str`
    - Mục đích: Build parent context by concatenating all sub-communities' contexts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/community_reports_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 103
- **Mô tả module**: A module containing 'CommunityReportsResult' and 'CommunityReportsExtractor' models.
- **Imports nổi bật**: logging, traceback, dataclasses (dataclass), typing (TYPE_CHECKING), pydantic (BaseModel, Field), graphrag.index.typing.error_handler (ErrorHandlerFn)
- **Class top-level**:
  - `FindingModel`
    - Mục đích: A model for the expected LLM response shape.
    - Được tham chiếu bởi (xấp xỉ): tests/verbs/test_create_community_reports.py
  - `CommunityReportResponse`
    - Mục đích: A model for the expected LLM response shape.
    - Được tham chiếu bởi (xấp xỉ): tests/verbs/test_create_community_reports.py
  - `CommunityReportsResult`
    - Mục đích: Community reports result class definition.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `CommunityReportsExtractor`
    - Mục đích: Community reports extractor class definition.
    - Methods chính: __init__, __call__, _get_text_output
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/explode_communities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 24
- **Mô tả module**: Explode a list of communities into nodes for filtering.
- **Imports nổi bật**: pandas, graphrag.data_model.schemas (COMMUNITY_ID)
- **Hàm top-level**:
  - `explode_communities(communities, entities) -> pd.DataFrame`
    - Mục đích: Explode a list of communities into nodes for filtering.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 165
- **Mô tả module**: A module containing summarize_communities method definition.
- **Imports nổi bật**: logging, collections.abc (Callable), typing (TYPE_CHECKING), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas, graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.index.operations.summarize_communities.community_reports_extractor (CommunityReportsExtractor), graphrag.index.operations.summarize_communities.typing (CommunityReport, CommunityReportsStrategy, Finding), graphrag.index.operations.summarize_communities.utils (get_levels)
- **Hàm top-level**:
  - `summarize_communities(nodes, communities, local_contexts, level_context_builder, callbacks, model, prompt, tokenizer, max_input_length, max_report_length, num_threads, async_type)`
    - Mục đích: Generate community summaries.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/build_mixed_context.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_generate_report(runner, model, extraction_prompt, community_id, community_level, community_context, max_report_length) -> CommunityReport | None`
    - Mục đích: Generate a report for a single community.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_extractor(community, input, level, model, extraction_prompt, max_report_length) -> CommunityReport | None`
    - Mục đích: Run the graph intelligence entity extraction strategy.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/typing.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 50
- **Mô tả module**: A module containing 'Finding' and 'CommunityReport' models.
- **Imports nổi bật**: collections.abc (Awaitable, Callable), typing (TYPE_CHECKING, Any), typing_extensions (TypedDict)
- **Class top-level**:
  - `Finding`
    - Mục đích: Finding class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, tests/fixtures/min-csv/input/dulce.csv
  - `CommunityReport`
    - Mục đích: Community report class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/data_model/community_report.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, packages/graphrag/graphrag/query/context_builder/community_context.py, packages/graphrag/graphrag/query/context_builder/dynamic_community_selection.py, packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/indexer_adapters.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/utils.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 18
- **Mô tả module**: A module containing community report generation utilities.
- **Imports nổi bật**: pandas, graphrag.data_model.schemas
- **Hàm top-level**:
  - `get_levels(df, level_column) -> list[int]`
    - Mục đích: Get the levels of the communities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/summarize_communities/graph_context`

- Số file: **3**

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Package of context builders for graph-based reports.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 369
- **Mô tả module**: Context builders for graphs.
- **Imports nổi bật**: logging, typing (cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas, graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.operations.summarize_communities.build_mixed_context (build_mixed_context), graphrag.index.operations.summarize_communities.graph_context.sort_context (parallel_sort_context_batch, sort_context), graphrag.index.operations.summarize_communities.utils (get_levels), graphrag.index.utils.dataframes (antijoin, drop_columns, join, select, transform_series, union, where_column_equals), graphrag.logger.progress (progress_iterable)
- **Hàm top-level**:
  - `build_local_context(nodes, edges, claims, tokenizer, callbacks, max_context_tokens)`
    - Mục đích: Prep communities for report generation.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prepare_reports_at_level(node_df, edge_df, claim_df, tokenizer, level, max_context_tokens) -> pd.DataFrame`
    - Mục đích: Prepare reports at a given level.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `build_level_context(report_df, community_hierarchy_df, local_context_df, tokenizer, level, max_context_tokens) -> pd.DataFrame`
    - Mục đích: Prep context for each community in a given level.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_drop_community_level(df) -> pd.DataFrame`
    - Mục đích: Drop the community level column from the dataframe.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_at_level(level, df) -> pd.DataFrame`
    - Mục đích: Return records at the given level.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_antijoin_reports(df, reports) -> pd.DataFrame`
    - Mục đích: Return records in df that are not in reports.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_sort_and_trim_context(df, tokenizer, max_context_tokens) -> pd.Series`
    - Mục đích: Sort and trim context to fit the limit.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_build_mixed_context(df, tokenizer, max_context_tokens) -> pd.Series`
    - Mục đích: Sort and trim context to fit the limit.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_subcontext_df(level, report_df, local_context_df) -> pd.DataFrame`
    - Mục đích: Get sub-community context for each community.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_community_df(level, invalid_context_df, sub_context_df, community_hierarchy_df, tokenizer, max_context_tokens) -> pd.DataFrame`
    - Mục đích: Get community context for each community.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/sort_context.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 165
- **Mô tả module**: Sort context by degree in descending order.
- **Imports nổi bật**: pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas
- **Hàm top-level**:
  - `sort_context(local_context, tokenizer, sub_community_reports, max_context_tokens, node_name_column, node_details_column, edge_id_column, edge_details_column, edge_degree_column, edge_source_column, edge_target_column, claim_details_column) -> str`
    - Mục đích: Sort context by degree in descending order, optimizing for performance.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/build_mixed_context.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py, tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `parallel_sort_context_batch(community_df, tokenizer, max_context_tokens, parallel)`
    - Mục đích: Calculate context using parallelization if enabled.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context`

- Số file: **4**

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Package of context builders for text unit-based reports.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 238
- **Mô tả module**: Context builders for text units.
- **Imports nổi bật**: logging, typing (cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas, graphrag.index.operations.summarize_communities.build_mixed_context (build_mixed_context), graphrag.index.operations.summarize_communities.text_unit_context.prep_text_units (prep_text_units), graphrag.index.operations.summarize_communities.text_unit_context.sort_context (sort_context)
- **Hàm top-level**:
  - `build_local_context(community_membership_df, text_units_df, node_df, tokenizer, max_context_tokens) -> pd.DataFrame`
    - Mục đích: Prep context data for community report generation using text unit data.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `build_level_context(report_df, community_hierarchy_df, local_context_df, level, tokenizer, max_context_tokens) -> pd.DataFrame`
    - Mục đích: Prep context for each community in a given level.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/prep_text_units.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 47
- **Mô tả module**: Prepare text units for community reports.
- **Imports nổi bật**: logging, pandas, graphrag.data_model.schemas
- **Hàm top-level**:
  - `prep_text_units(text_unit_df, node_df) -> pd.DataFrame`
    - Mục đích: Calculate text unit degree  and concatenate text unit details.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 86
- **Mô tả module**: Sort local context by total degree of associated nodes in descending order.
- **Imports nổi bật**: logging, pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas
- **Hàm top-level**:
  - `get_context_string(text_units, sub_community_reports) -> str`
    - Mục đích: Concatenate structured data into a context string.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `sort_context(local_context, tokenizer, sub_community_reports, max_context_tokens) -> str`
    - Mục đích: Sort local context (list of text units) by total degree of associated nodes in descending order.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/build_mixed_context.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/sort_context.py, packages/graphrag/graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py, tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/operations/summarize_descriptions`

- Số file: **4**

#### File: `packages/graphrag/graphrag/index/operations/summarize_descriptions/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Root package for description summarization.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_descriptions/description_summary_extractor.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 135
- **Mô tả module**: A module containing 'SummarizationResult' and 'SummarizeExtractor' models.
- **Imports nổi bật**: json, dataclasses (dataclass), typing (TYPE_CHECKING), graphrag.index.typing.error_handler (ErrorHandlerFn)
- **Class top-level**:
  - `SummarizationResult`
    - Mục đích: Unipartite graph extraction result class definition.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `SummarizeExtractor`
    - Mục đích: Unipartite graph extractor class definition.
    - Methods chính: __init__, __call__, _summarize_descriptions, _summarize_descriptions_with_llm
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 141
- **Mô tả module**: A module containing the summarize_descriptions verb.
- **Imports nổi bật**: asyncio, logging, typing (TYPE_CHECKING), pandas, graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.operations.summarize_descriptions.description_summary_extractor (SummarizeExtractor), graphrag.index.operations.summarize_descriptions.typing (SummarizedDescriptionResult), graphrag.logger.progress (ProgressTicker, progress_ticker)
- **Hàm top-level**:
  - `summarize_descriptions(entities_df, relationships_df, callbacks, model, max_summary_length, max_input_tokens, prompt, num_threads) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Summarize entity and relationship descriptions from an entity graph, using a language model.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/cli/initialize.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/config/models/summarize_descriptions_config.py, packages/graphrag/graphrag/index/workflows/extract_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_summarize_descriptions(id, descriptions, model, max_summary_length, max_input_tokens, prompt) -> SummarizedDescriptionResult`
    - Mục đích: Run the graph intelligence entity extraction strategy.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/operations/summarize_descriptions/typing.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 22
- **Mô tả module**: A module containing 'SummarizedDescriptionResult' model.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any, NamedTuple)
- **Class top-level**:
  - `SummarizedDescriptionResult`
    - Mục đích: Entity summarization result class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py
  - `DescriptionSummarizeRow`
    - Mục đích: DescriptionSummarizeRow class definition.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/run`

- Số file: **4**

#### File: `packages/graphrag/graphrag/index/run/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Run module for GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/run/profiling.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 61
- **Mô tả module**: Workflow profiling utilities.
- **Imports nổi bật**: time, tracemalloc, types (TracebackType), typing (Self), graphrag.index.typing.stats (WorkflowMetrics)
- **Class top-level**:
  - `WorkflowProfiler`
    - Mục đích: Context manager for profiling workflow execution.
    - Methods chính: __init__, __enter__, __exit__, metrics
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/run_pipeline.py, tests/unit/indexing/test_profiling.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/run/run_pipeline.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 189
- **Mô tả module**: Different methods to run the pipeline.
- **Imports nổi bật**: json, logging, time, collections.abc (AsyncIterable), dataclasses (asdict), typing (Any), pandas, graphrag_cache (create_cache), graphrag_storage (create_storage), graphrag_storage.tables.table_provider (TableProvider), graphrag_storage.tables.table_provider_factory (create_table_provider), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks)
- **Hàm top-level**:
  - `run_pipeline(pipeline, config, callbacks, is_update_run, additional_context, input_documents) -> AsyncIterable[PipelineRunResult]`
    - Mục đích: Run all workflows using a simplified pipeline.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/index/run/profiling.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_run_pipeline(pipeline, config, context) -> AsyncIterable[PipelineRunResult]`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_dump_stats_json(context) -> None`
    - Mục đích: Dump stats state to storage.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_dump_context_json(context) -> None`
    - Mục đích: Dump context state to storage.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_copy_previous_output(output_table_provider, previous_table_provider) -> None`
    - Mục đích: Copy all parquet tables from output to previous storage for backup.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/run/utils.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 76
- **Mô tả module**: Utility functions for the GraphRAG run module.
- **Imports nổi bật**: graphrag_cache (Cache), graphrag_cache.memory_cache (MemoryCache), graphrag_storage (Storage, create_storage), graphrag_storage.memory_storage (MemoryStorage), graphrag_storage.tables.parquet_table_provider (ParquetTableProvider), graphrag_storage.tables.table_provider (TableProvider), graphrag_storage.tables.table_provider_factory (create_table_provider), graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.callbacks.workflow_callbacks_manager (WorkflowCallbacksManager), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext)
- **Hàm top-level**:
  - `create_run_context(input_storage, output_storage, output_table_provider, previous_table_provider, cache, callbacks, stats, state) -> PipelineRunContext`
    - Mục đích: Create the run context for the pipeline.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/run_pipeline.py, tests/verbs/test_pipeline_state.py, tests/verbs/util.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_callback_chain(callbacks) -> WorkflowCallbacks`
    - Mục đích: Create a callback manager that encompasses multiple callbacks.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_update_table_providers(config, timestamp) -> tuple[TableProvider, TableProvider, TableProvider]`
    - Mục đích: Get table providers for the update index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_communities.py, packages/graphrag/graphrag/index/workflows/update_community_reports.py, packages/graphrag/graphrag/index/workflows/update_covariates.py, packages/graphrag/graphrag/index/workflows/update_entities_relationships.py, packages/graphrag/graphrag/index/workflows/update_final_documents.py, packages/graphrag/graphrag/index/workflows/update_text_embeddings.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/text_splitting`

- Số file: **2**

#### File: `packages/graphrag/graphrag/index/text_splitting/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: The Indexing Engine Text Splitting package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/text_splitting/text_splitting.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 103
- **Mô tả module**: A module containing 'TokenTextSplitter' class and 'split_single_text_on_tokens' function.
- **Imports nổi bật**: logging, abc (ABC), collections.abc (Callable), typing (cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `split_single_text_on_tokens(text, tokens_per_chunk, chunk_overlap, encode, decode) -> list[str]`
    - Mục đích: Split a single text and return chunks using the tokenizer.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TokenTextSplitter`
    - Mục đích: Token text splitter class definition.
    - Methods chính: __init__, num_tokens, split_text
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/typing`

- Số file: **8**

#### File: `packages/graphrag/graphrag/index/typing/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Root typings for GraphRAG.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/context.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 35
- **Mô tả module**: A module containing the 'PipelineRunContext' models.
- **Imports nổi bật**: dataclasses (dataclass), graphrag_cache (Cache), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.index.typing.state (PipelineState), graphrag.index.typing.stats (PipelineRunStats), graphrag_storage (Storage, TableProvider)
- **Class top-level**:
  - `PipelineRunContext`
    - Mục đích: Provides the context for the current pipeline run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/run_pipeline.py, packages/graphrag/graphrag/index/run/utils.py, packages/graphrag/graphrag/index/typing/workflow.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/error_handler.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 9
- **Mô tả module**: Shared error handler types.
- **Imports nổi bật**: collections.abc (Callable)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/pipeline.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 28
- **Mô tả module**: A module containing the Pipeline class.
- **Imports nổi bật**: collections.abc (Generator), graphrag.index.typing.workflow (Workflow)
- **Class top-level**:
  - `Pipeline`
    - Mục đích: Encapsulates running workflows.
    - Methods chính: __init__, run, names, remove
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-llm/graphrag_llm/middleware/with_middleware_pipeline.py, packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, packages/graphrag/graphrag/callbacks/console_workflow_callbacks.py, packages/graphrag/graphrag/index/run/run_pipeline.py, packages/graphrag/graphrag/index/typing/pipeline_run_result.py, packages/graphrag/graphrag/index/typing/state.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/pipeline_run_result.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 23
- **Mô tả module**: A module containing the PipelineRunResult class.
- **Imports nổi bật**: dataclasses (dataclass), typing (Any), graphrag.index.typing.state (PipelineState)
- **Class top-level**:
  - `PipelineRunResult`
    - Mục đích: Pipeline run result class definition.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/callbacks/console_workflow_callbacks.py, packages/graphrag/graphrag/callbacks/noop_workflow_callbacks.py, packages/graphrag/graphrag/callbacks/workflow_callbacks.py, packages/graphrag/graphrag/callbacks/workflow_callbacks_manager.py, packages/graphrag/graphrag/index/run/run_pipeline.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/state.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 9
- **Mô tả module**: Pipeline state types.
- **Imports nổi bật**: typing (Any)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/stats.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 43
- **Mô tả module**: Pipeline stats types.
- **Imports nổi bật**: dataclasses (dataclass, field)
- **Class top-level**:
  - `WorkflowMetrics`
    - Mục đích: Metrics collected for a single workflow execution.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/profiling.py, tests/unit/indexing/test_profiling.py
  - `PipelineRunStats`
    - Mục đích: Pipeline running stats.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/utils.py, packages/graphrag/graphrag/index/typing/context.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/typing/workflow.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 29
- **Mô tả module**: Pipeline workflow types.
- **Imports nổi bật**: collections.abc (Awaitable, Callable), dataclasses (dataclass), typing (Any), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext)
- **Class top-level**:
  - `WorkflowFunctionOutput`
    - Mục đích: Data container for Workflow function results.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/update`

- Số file: **5**

#### File: `packages/graphrag/graphrag/index/update/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Incremental Indexing main module definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/update/communities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 152
- **Mô tả module**: Dataframe operations and utils for Incremental Indexing.
- **Imports nổi bật**: pandas, graphrag.data_model.schemas (COMMUNITIES_FINAL_COLUMNS, COMMUNITY_REPORTS_FINAL_COLUMNS)
- **Hàm top-level**:
  - `_update_and_merge_communities(old_communities, delta_communities) -> tuple[pd.DataFrame, dict]`
    - Mục đích: Update and merge communities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_and_merge_community_reports(old_community_reports, delta_community_reports, community_id_mapping) -> pd.DataFrame`
    - Mục đích: Update and merge community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_community_reports.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/update/entities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 78
- **Mô tả module**: Entity related operations and utils for Incremental Indexing.
- **Imports nổi bật**: itertools, numpy, pandas, graphrag.data_model.schemas (ENTITIES_FINAL_COLUMNS)
- **Hàm top-level**:
  - `_group_and_resolve_entities(old_entities_df, delta_entities_df) -> tuple[pd.DataFrame, dict]`
    - Mục đích: Group and resolve entities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_entities_relationships.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/update/incremental_index.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 79
- **Mô tả module**: Dataframe operations and utils for Incremental Indexing.
- **Imports nổi bật**: dataclasses (dataclass), numpy, pandas, graphrag_storage.tables.table_provider (TableProvider)
- **Hàm top-level**:
  - `get_delta_docs(input_dataset, table_provider) -> InputDelta`
    - Mục đích: Get the delta between the input dataset and the final documents.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/load_update_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `concat_dataframes(name, previous_table_provider, delta_table_provider, output_table_provider) -> pd.DataFrame`
    - Mục đích: Concatenate dataframes.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `InputDelta`
    - Mục đích: Dataclass to hold the input delta.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/update/relationships.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 87
- **Mô tả module**: Relationship related operations and utils for Incremental Indexing.
- **Imports nổi bật**: itertools, numpy, pandas, graphrag.data_model.schemas (RELATIONSHIPS_FINAL_COLUMNS)
- **Hàm top-level**:
  - `_update_and_merge_relationships(old_relationships, delta_relationships) -> pd.DataFrame`
    - Mục đích: Update and merge relationships.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_entities_relationships.py, tests/unit/indexing/update/test_update_relationships.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/utils`

- Số file: **8**

#### File: `packages/graphrag/graphrag/index/utils/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 5
- **Mô tả module**: Utils methods definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/dataframes.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 54
- **Mô tả module**: A module containing DataFrame utilities.
- **Imports nổi bật**: collections.abc (Callable), typing (Any, cast), pandas, pandas._typing (MergeHow)
- **Hàm top-level**:
  - `drop_columns(df, *column) -> pd.DataFrame`
    - Mục đích: Drop columns from a dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `where_column_equals(df, column, value) -> pd.DataFrame`
    - Mục đích: Return a filtered DataFrame where a column equals a value.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `antijoin(df, exclude, column) -> pd.DataFrame`
    - Mục đích: Return an anti-joined dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `transform_series(series, fn) -> pd.Series`
    - Mục đích: Apply a transformation function to a series.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `join(left, right, key, strategy) -> pd.DataFrame`
    - Mục đích: Perform a table join.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-chunking/graphrag_chunking/chunker_factory.py, packages/graphrag-chunking/graphrag_chunking/transformers.py, packages/graphrag-common/graphrag_common/factory/factory.py, packages/graphrag-input/graphrag_input/hashing.py, packages/graphrag-input/graphrag_input/input_reader_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `union(*frames) -> pd.DataFrame`
    - Mục đích: Perform a union operation on the given set of dataframes.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/graphs/connected_components.py, packages/graphrag/graphrag/graphs/modularity.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py, packages/graphrag/graphrag/query/context_builder/entity_extraction.py, tests/unit/graphs/test_stable_lcc.py, tests/unit/indexing/test_cluster_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `select(df, *columns) -> pd.DataFrame`
    - Mục đích: Select columns from a dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/README.md, packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb, packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb, packages/graphrag-vectors/example_notebooks/lancedb.ipynb, packages/graphrag-vectors/graphrag_vectors/azure_ai_search.py, packages/graphrag-vectors/graphrag_vectors/cosmosdb.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/derive_from_rows.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 168
- **Mô tả module**: A module containing derive_from_rows, derive_from_rows_asyncio_threads, and derive_from_rows_asyncio methods.
- **Imports nổi bật**: asyncio, inspect, logging, traceback, collections.abc (Awaitable, Callable, Coroutine, Hashable), typing (Any, TypeVar, cast), pandas, graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.logger.progress (progress_ticker)
- **Hàm top-level**:
  - `derive_from_rows(input, transform, callbacks, num_threads, async_type, progress_msg) -> list[ItemType | None]`
    - Mục đích: Apply a generic transform function to each row. Any errors will be reported and thrown.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py, packages/graphrag/graphrag/index/operations/extract_graph/extract_graph.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `derive_from_rows_asyncio_threads(input, transform, callbacks, num_threads, progress_msg) -> list[ItemType | None]`
    - Mục đích: Derive from rows asynchronously.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `derive_from_rows_asyncio(input, transform, callbacks, num_threads, progress_msg) -> list[ItemType | None]`
    - Mục đích: Derive from rows asynchronously.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_derive_from_rows_base(input, transform, callbacks, gather, progress_msg) -> list[ItemType | None]`
    - Mục đích: Derive from rows asynchronously.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `ParallelizationError`
    - Mục đích: Exception for invalid parallel processing.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/dicts.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 23
- **Mô tả module**: A utility module containing methods for inspecting and verifying dictionary types.
- **Hàm top-level**:
  - `dict_has_keys_with_types(data, expected_fields, inplace) -> bool`
    - Mục đích: Return True if the given dictionary has the given keys with the given types.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/hashing.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 15
- **Mô tả module**: Hashing utilities.
- **Imports nổi bật**: collections.abc (Iterable), hashlib (sha512), typing (Any)
- **Hàm top-level**:
  - `gen_sha512_hash(item, hashcode)`
    - Mục đích: Generate a SHA512 hash.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-input/graphrag_input/hashing.py, packages/graphrag-input/graphrag_input/markitdown.py, packages/graphrag-input/graphrag_input/structured_file_reader.py, packages/graphrag-input/graphrag_input/text.py, packages/graphrag/graphrag/index/operations/build_noun_graph/build_noun_graph.py, packages/graphrag/graphrag/index/operations/finalize_community_reports.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/is_null.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 20
- **Mô tả module**: Defines the is_null utility.
- **Imports nổi bật**: math, typing (Any)
- **Hàm top-level**:
  - `is_null(value) -> bool`
    - Mục đích: Check if value is null or is nan.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/string.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 20
- **Mô tả module**: String utilities.
- **Imports nổi bật**: html, re, typing (Any)
- **Hàm top-level**:
  - `clean_str(input) -> str`
    - Mục đích: Clean an input string by removing HTML escapes, control characters, and other unwanted characters.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_graph/graph_extractor.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/utils/uuid.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 15
- **Mô tả module**: UUID utilities.
- **Imports nổi bật**: uuid, random (Random, getrandbits)
- **Hàm top-level**:
  - `gen_uuid(rd)`
    - Mục đích: Generate a random UUID v4.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/index/workflows`

- Số file: **24**

#### File: `packages/graphrag/graphrag/index/workflows/__init__.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 101
- **Mô tả module**: A package containing all built-in workflow definitions.
- **Imports nổi bật**: graphrag.index.workflows.factory (PipelineFactory), create_base_text_units (run_workflow), create_communities (run_workflow), create_community_reports (run_workflow), create_community_reports_text (run_workflow), create_final_documents (run_workflow), create_final_text_units (run_workflow), extract_covariates (run_workflow), extract_graph (run_workflow), extract_graph_nlp (run_workflow), finalize_graph (run_workflow), generate_text_embeddings (run_workflow)
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_base_text_units.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 161
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, typing (Any), graphrag_chunking.chunker (Chunker), graphrag_chunking.chunker_factory (create_chunker), graphrag_chunking.transformers (add_metadata), graphrag_input (TextDocument), graphrag_llm.tokenizer (Tokenizer), graphrag_storage.tables.table (Table), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to transform base text_units.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_base_text_units(documents_table, text_units_table, total_rows, callbacks, tokenizer, chunker, prepend_metadata) -> list[dict[str, Any]]`
    - Mục đích: Transform documents into chunked text units via streaming read/write.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, packages/graphrag/graphrag/prompt_tune/loader/input.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/verbs/test_create_base_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `chunk_document(doc, chunker, prepend_metadata) -> list[str]`
    - Mục đích: Chunk a single document row into text fragments.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/prompt_tune/loader/input.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_communities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 208
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, datetime (datetime, timezone), typing (Any, cast), uuid (uuid4), numpy, pandas, graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.data_model.schemas (COMMUNITIES_FINAL_COLUMNS), graphrag.index.operations.cluster_graph (cluster_graph), graphrag.index.typing.context (PipelineRunContext)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to transform final communities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_communities(communities_table, entities_table, relationships, max_cluster_size, use_lcc, seed) -> list[dict[str, Any]]`
    - Mục đích: Build communities from clustered relationships and stream rows to the table.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/unit/indexing/test_create_communities.py, tests/verbs/test_create_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_sanitize_row(row) -> dict[str, Any]`
    - Mục đích: Convert numpy types to native Python types for table serialization.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_create_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_community_reports.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 200
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING), pandas, graphrag_llm.completion (create_completion), graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.schemas, graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.operations.finalize_community_reports (finalize_community_reports)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to transform community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_community_reports(relationships, entities, communities, claims_input, callbacks, model, tokenizer, prompt, max_input_length, max_report_length, num_threads, async_type) -> pd.DataFrame`
    - Mục đích: All the steps to transform community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/verbs/test_create_community_reports.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prep_nodes(input) -> pd.DataFrame`
    - Mục đích: Prepare nodes by filtering, filling missing descriptions, and creating NODE_DETAILS.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prep_edges(input) -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prep_claims(input) -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_community_reports_text.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 120
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING), pandas, graphrag_llm.completion (create_completion), graphrag_llm.tokenizer (Tokenizer), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.operations.finalize_community_reports (finalize_community_reports), graphrag.index.operations.summarize_communities.explode_communities (explode_communities)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to transform community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_community_reports_text(entities, communities, text_units, callbacks, model, tokenizer, prompt, max_input_length, max_report_length, num_threads, async_type) -> pd.DataFrame`
    - Mục đích: All the steps to transform community reports.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/text/config.json
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_final_documents.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 74
- **Mô tả module**: Workflow to create final documents with text unit mappings.
- **Imports nổi bật**: logging, typing (Any), graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.row_transformers (transform_document_row), graphrag.data_model.schemas (DOCUMENTS_FINAL_COLUMNS), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(_config, context) -> WorkflowFunctionOutput`
    - Mục đích: Transform final documents via streaming Table reads/writes.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_final_documents(text_units_table, documents_table, output_table) -> list[dict[str, Any]]`
    - Mục đích: Build text-unit mapping, then stream-enrich documents.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/verbs/test_create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/create_final_text_units.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 136
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, contextlib (nullcontext), typing (Any), graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.row_transformers (transform_entity_row, transform_relationship_row, transform_text_unit_row), graphrag.data_model.schemas (TEXT_UNITS_FINAL_COLUMNS), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to transform the text units.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_final_text_units(text_units_table, entities_table, relationships_table, output_table, covariates_table) -> list[dict[str, Any]]`
    - Mục đích: Enrich text units with entity, relationship, and covariate id lookups.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/unit/storage/test_csv_table.py, tests/verbs/test_create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_build_multi_ref_map(table) -> dict[str, list[str]]`
    - Mục đích: Build a text_unit_id -> [row_id] reverse lookup from a table with a text_unit_ids list field.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_build_covariate_map(table) -> dict[str, list[str]]`
    - Mục đích: Build a text_unit_id -> [covariate_id] reverse lookup from the covariate table.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/extract_covariates.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 109
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING), uuid (uuid4), pandas, graphrag_llm.completion (create_completion), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.defaults (DEFAULT_ENTITY_TYPES), graphrag.config.enums (AsyncType), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.data_model.schemas (COVARIATES_FINAL_COLUMNS)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to extract and format covariates.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `extract_covariates(text_units, callbacks, model, covariate_type, max_gleanings, claim_description, prompt, entity_types, num_threads, async_type) -> pd.DataFrame`
    - Mục đích: All the steps to extract and format covariates.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/extract_covariates/extract_covariates.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/verbs/test_extract_covariates.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/extract_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 186
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING), pandas, graphrag_llm.completion (create_completion), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.enums (AsyncType), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.operations.extract_graph.extract_graph (extract_graph), graphrag.index.operations.summarize_descriptions.summarize_descriptions (summarize_descriptions), graphrag.index.typing.context (PipelineRunContext)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to create the base entity graph.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `extract_graph(text_units, callbacks, extraction_model, extraction_prompt, entity_types, max_gleanings, extraction_num_threads, extraction_async_type, summarization_model, max_summary_length, max_input_tokens, summarization_prompt, summarization_num_threads) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]`
    - Mục đích: All the steps to create the base entity graph.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/azure_cosmos_storage.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/cli/initialize.py, packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/extract_graph_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_summarized_entities_relationships(extracted_entities, extracted_relationships, callbacks, model, max_summary_length, max_input_tokens, summarization_prompt, num_threads) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Summarize the entities and relationships.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/update_entities_relationships.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/extract_graph_nlp.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 143
- **Mô tả module**: NLP-based graph extraction workflow.
- **Imports nổi bật**: logging, typing (Any), pandas, graphrag_cache (Cache), graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.operations.build_noun_graph.build_noun_graph (build_noun_graph), graphrag.index.operations.build_noun_graph.np_extractors.base (BaseNounPhraseExtractor), graphrag.index.operations.build_noun_graph.np_extractors.factory (create_noun_phrase_extractor), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Run the NLP graph-extraction pipeline.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `extract_graph_nlp(text_units_table, cache, entities_table, relationships_table, text_analyzer, normalize_edge_weights) -> dict[str, list[dict[str, Any]]]`
    - Mục đích: Extract noun-phrase graph and stream results to output tables.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/init_content.py, packages/graphrag/graphrag/config/models/extract_graph_nlp_config.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_write_entities(nodes_df, table) -> list[dict[str, Any]]`
    - Mục đích: Stream entity rows into the output table.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_write_relationships(edges_df, table) -> list[dict[str, Any]]`
    - Mục đích: Stream relationship rows into the output table.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/factory.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 98
- **Mô tả module**: Encapsulates pipeline construction and selection.
- **Imports nổi bật**: logging, typing (ClassVar), graphrag.config.enums (IndexingMethod), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.pipeline (Pipeline), graphrag.index.typing.workflow (WorkflowFunction)
- **Class top-level**:
  - `PipelineFactory`
    - Mục đích: A factory class for workflow pipelines.
    - Methods chính: register, register_all, register_pipeline, create_pipeline
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/index/workflows/__init__.py, tests/verbs/test_pipeline_state.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/finalize_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 126
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, collections (Counter), typing (Any), graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.row_transformers (transform_entity_row, transform_relationship_row), graphrag.index.operations.finalize_entities (finalize_entities), graphrag.index.operations.finalize_relationships (finalize_relationships), graphrag.index.operations.snapshot_graphml (snapshot_graphml), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to create the base entity graph.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `finalize_graph(entities_table, relationships_table) -> dict[str, list[dict[str, Any]]]`
    - Mục đích: Compute degrees and finalize entities and relationships.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/unit/indexing/test_finalize_graph.py, tests/verbs/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_build_degree_map(relationships_table) -> dict[str, int]`
    - Mục đích: Stream relationship rows to compute node degrees.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/generate_text_embeddings.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 163
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, contextlib (AsyncExitStack), dataclasses (dataclass), typing (TYPE_CHECKING), graphrag_llm.embedding (create_embedding), graphrag_storage.tables.table (RowTransformer), graphrag_vectors (create_vector_store), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.embeddings (community_full_content_embedding, entity_description_embedding, text_unit_text_embedding), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.row_transformers (transform_entity_row_for_embedding)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Generate text embeddings for configured fields via streaming Tables.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `generate_text_embeddings(config, table_provider, callbacks, model, tokenizer) -> None`
    - Mục đích: Generate text embeddings for all configured fields.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, packages/graphrag/graphrag/index/workflows/update_text_embeddings.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json, tests/verbs/test_generate_text_embeddings.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `EmbeddingFieldConfig`
    - Mục đích: Configuration for a single embedding field.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/load_input_documents.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 61
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, dataclasses (asdict), pandas, graphrag_input (InputReader, create_input_reader), graphrag_storage.tables.table (Table), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Load and parse input documents into a standard format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_input_documents(input_reader, documents_table, sample_size) -> tuple[pd.DataFrame, int]`
    - Mục đích: Load and parse input documents into a standard format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/run_pipeline.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py, tests/fixtures/min-csv/config.json, tests/fixtures/text/config.json
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/load_update_documents.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 63
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, dataclasses (asdict), pandas, graphrag_input.input_reader (InputReader), graphrag_input.input_reader_factory (create_input_reader), graphrag_storage.tables.table_provider (TableProvider), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.update.incremental_index (get_delta_docs)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Load and parse update-only input documents into a standard format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_update_documents(input_reader, previous_table_provider) -> pd.DataFrame`
    - Mục đích: Load and parse update-only input documents into a standard format.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/run/run_pipeline.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/prune_graph.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 79
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, pandas, graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.config.models.prune_graph_config (PruneGraphConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.operations.prune_graph (prune_graph), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: All the steps to create the base entity graph.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `prune_graph(entities, relationships, pruning_config) -> tuple[pd.DataFrame, pd.DataFrame]`
    - Mục đích: Prune a full graph based on graph statistics.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/config/defaults.py, packages/graphrag/graphrag/config/models/graph_rag_config.py, packages/graphrag/graphrag/config/models/prune_graph_config.py, packages/graphrag/graphrag/index/operations/prune_graph.py, packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_clean_state.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 32
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(_config, context) -> WorkflowFunctionOutput`
    - Mục đích: Clean the state after the update.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_communities.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 55
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, graphrag_storage.tables.table_provider (TableProvider), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.update.communities (_update_and_merge_communities)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the communities from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_communities(previous_table_provider, delta_table_provider, output_table_provider) -> dict`
    - Mục đích: Update the communities output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_community_reports.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 68
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, pandas, graphrag_storage.tables.table_provider (TableProvider), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.update.communities (_update_and_merge_community_reports)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the community reports from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_community_reports(previous_table_provider, delta_table_provider, output_table_provider, community_id_mapping) -> pd.DataFrame`
    - Mục đích: Update the community reports output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_covariates.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 81
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, numpy, pandas, graphrag_storage.tables.table_provider (TableProvider), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the covariates from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_covariates(previous_table_provider, delta_table_provider, output_table_provider) -> None`
    - Mục đích: Update the covariates output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_merge_covariates(old_covariates, delta_covariates) -> pd.DataFrame`
    - Mục đích: Merge the covariates.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_entities_relationships.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 120
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, pandas, graphrag_cache (Cache), graphrag_llm.completion (create_completion), graphrag_storage.tables.table_provider (TableProvider), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.callbacks.workflow_callbacks (WorkflowCallbacks), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.operations.extract_graph.utils (filter_orphan_relationships), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the entities and relationships from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_entities_and_relationships(previous_table_provider, delta_table_provider, output_table_provider, config, cache, callbacks) -> tuple[pd.DataFrame, pd.DataFrame, dict]`
    - Mục đích: Update Final Entities  and Relationships output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_final_documents.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 38
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.update.incremental_index (concat_dataframes)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the documents from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_text_embeddings.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 53
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, graphrag_llm.embedding (create_embedding), graphrag.cache.cache_key_creator (cache_key_creator), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.workflows.generate_text_embeddings (generate_text_embeddings)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update text embeddings for an incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/index/workflows/update_text_units.py`
- **Loại**: python
- **Vai trò**: Pipeline indexing: đọc input, trích graph, cộng đồng, báo cáo, embedding.
- **Số dòng**: 96
- **Mô tả module**: A module containing run_workflow method definition.
- **Imports nổi bật**: logging, numpy, pandas, graphrag_storage.tables.table_provider (TableProvider), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.data_reader (DataReader), graphrag.index.run.utils (get_update_table_providers), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput)
- **Hàm top-level**:
  - `run_workflow(config, context) -> WorkflowFunctionOutput`
    - Mục đích: Update the text units from a incremental index run.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/workflows/__init__.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/index/workflows/create_communities.py, packages/graphrag/graphrag/index/workflows/create_community_reports.py, packages/graphrag/graphrag/index/workflows/create_community_reports_text.py, packages/graphrag/graphrag/index/workflows/create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_text_units(previous_table_provider, delta_table_provider, output_table_provider, entity_id_mapping) -> pd.DataFrame`
    - Mục đích: Update the text units output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_update_and_merge_text_units(old_text_units, delta_text_units, entity_id_mapping) -> pd.DataFrame`
    - Mục đích: Update and merge text units.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/logger`

- Số file: **5**

#### File: `packages/graphrag/graphrag/logger/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Logger utilities and implementations.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/logger/blob_workflow_logger.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 120
- **Mô tả module**: A logger that emits updates from the indexing engine to a blob in Azure Storage.
- **Imports nổi bật**: json, logging, datetime (datetime, timezone), pathlib (Path), typing (Any), azure.identity (DefaultAzureCredential), azure.storage.blob (BlobServiceClient)
- **Class top-level**:
  - `BlobWorkflowLogger`
    - Mục đích: A logging handler that writes to a blob storage account.
    - Methods chính: __init__, emit, _get_log_type, _write_log
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/logger/factory.py, tests/integration/logging/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/logger/factory.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 65
- **Mô tả module**: Factory functions for creating a logger.
- **Imports nổi bật**: __future__ (annotations), logging, pathlib (Path), graphrag_common.factory (Factory), graphrag.config.enums (ReportingType)
- **Hàm top-level**:
  - `create_file_logger(**kwargs) -> logging.Handler`
    - Mục đích: Create a file-based logger.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_blob_logger(**kwargs) -> logging.Handler`
    - Mục đích: Create a blob storage-based logger.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `LoggerFactory`
    - Mục đích: A factory class for logger implementations.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/logger/standard_logging.py, tests/integration/logging/test_factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/logger/progress.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 96
- **Mô tả module**: Progress Logging Utilities.
- **Imports nổi bật**: logging, collections.abc (Callable, Iterable), dataclasses (dataclass), typing (TypeVar)
- **Hàm top-level**:
  - `progress_ticker(callback, num_total, description) -> ProgressTicker`
    - Mục đích: Create a progress ticker.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py, packages/graphrag/graphrag/index/operations/summarize_communities/summarize_communities.py, packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py, packages/graphrag/graphrag/index/utils/derive_from_rows.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `progress_iterable(iterable, progress, num_total, description) -> Iterable[T]`
    - Mục đích: Wrap an iterable with a progress handler. Every time an item is yielded, the progress handler will be called with the current progress.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `Progress`
    - Mục đích: A class representing the progress of a task.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/azure_cosmos_storage.py, packages/graphrag/graphrag/callbacks/console_workflow_callbacks.py, packages/graphrag/graphrag/callbacks/noop_workflow_callbacks.py, packages/graphrag/graphrag/callbacks/workflow_callbacks.py, packages/graphrag/graphrag/callbacks/workflow_callbacks_manager.py
  - `ProgressTicker`
    - Mục đích: A class that emits progress reports incrementally.
    - Methods chính: __init__, __call__, done
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/index/operations/embed_text/run_embed_text.py, packages/graphrag/graphrag/index/operations/summarize_descriptions/summarize_descriptions.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/logger/standard_logging.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 92
- **Mô tả module**: Standard logging configuration for the graphrag package.
- **Imports nổi bật**: __future__ (annotations), logging, typing (TYPE_CHECKING), graphrag.logger.factory (LoggerFactory)
- **Hàm top-level**:
  - `init_loggers(config, verbose, filename) -> None`
    - Mục đích: Initialize logging handlers for graphrag based on configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/index.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/api/query.py, packages/graphrag/graphrag/cli/index.py, packages/graphrag/graphrag/cli/prompt_tune.py, tests/integration/logging/test_standard_logging.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompt_tune`

- Số file: **3**

#### File: `packages/graphrag/graphrag/prompt_tune/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: The prompt-tuning package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/defaults.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 21
- **Mô tả module**: Default values for the prompt-tuning module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 20
- **Mô tả module**: Types for prompt tuning.
- **Imports nổi bật**: enum (Enum)
- **Class top-level**:
  - `DocSelectionType`
    - Mục đích: The type of document selection to use.
    - Methods chính: __str__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/__init__.py, packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/cli/main.py, packages/graphrag/graphrag/cli/prompt_tune.py, packages/graphrag/graphrag/prompt_tune/loader/input.py, tests/unit/prompt_tune/test_load_docs_in_chunks.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompt_tune/generator`

- Số file: **11**

#### File: `packages/graphrag/graphrag/prompt_tune/generator/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Prompt generation module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/community_report_rating.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 42
- **Mô tả module**: Generate a rating description for community report rating.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag.prompt_tune.prompt.community_report_rating (GENERATE_REPORT_RATING_PROMPT)
- **Hàm top-level**:
  - `generate_community_report_rating(model, domain, persona, docs) -> str`
    - Mục đích: Generate an LLM persona to use for GraphRAG prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/community_report_summarization.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 51
- **Mô tả module**: Module for generating prompts for community report summarization.
- **Imports nổi bật**: pathlib (Path), graphrag.prompt_tune.template.community_report_summarization (COMMUNITY_REPORT_SUMMARIZATION_PROMPT)
- **Hàm top-level**:
  - `create_community_summarization_prompt(persona, role, report_rating_description, language, output_path) -> str`
    - Mục đích: Create a prompt for community summarization. If output_path is provided, write the prompt to a file.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/community_reporter_role.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 43
- **Mô tả module**: Generate a community reporter role for community summarization.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag.prompt_tune.prompt.community_reporter_role (GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT)
- **Hàm top-level**:
  - `generate_community_reporter_role(model, domain, persona, docs) -> str`
    - Mục đích: Generate an LLM persona to use for GraphRAG prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/domain.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 35
- **Mô tả module**: Domain generation for GraphRAG prompts.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag.prompt_tune.prompt.domain (GENERATE_DOMAIN_PROMPT)
- **Hàm top-level**:
  - `generate_domain(model, docs) -> str`
    - Mục đích: Generate an LLM persona to use for GraphRAG prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/entity_relationship.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 79
- **Mô tả module**: Entity relationship example generation module.
- **Imports nổi bật**: asyncio, typing (TYPE_CHECKING), graphrag_llm.utils (CompletionMessagesBuilder), graphrag.prompt_tune.prompt.entity_relationship (ENTITY_RELATIONSHIPS_GENERATION_JSON_PROMPT, ENTITY_RELATIONSHIPS_GENERATION_PROMPT, UNTYPED_ENTITY_RELATIONSHIPS_GENERATION_PROMPT)
- **Hàm top-level**:
  - `generate_entity_relationship_examples(model, persona, entity_types, docs, language, json_mode) -> list[str]`
    - Mục đích: Generate a list of entity/relationships examples for use in generating an entity configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/entity_summarization_prompt.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 40
- **Mô tả module**: Entity summarization prompt generation module.
- **Imports nổi bật**: pathlib (Path), graphrag.prompt_tune.template.entity_summarization (ENTITY_SUMMARIZATION_PROMPT)
- **Hàm top-level**:
  - `create_entity_summarization_prompt(persona, language, output_path) -> str`
    - Mục đích: Create a prompt for entity summarization.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/entity_types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 75
- **Mô tả module**: Entity type generation module for fine-tuning.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag_llm.utils (CompletionMessagesBuilder), pydantic (BaseModel), graphrag.prompt_tune.defaults (DEFAULT_TASK), graphrag.prompt_tune.prompt.entity_types (ENTITY_TYPE_GENERATION_JSON_PROMPT, ENTITY_TYPE_GENERATION_PROMPT)
- **Hàm top-level**:
  - `generate_entity_types(model, domain, persona, docs, task, json_mode) -> str | list[str]`
    - Mục đích: Generate entity type categories from a given set of (small) documents.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `EntityTypesResponse`
    - Mục đích: Entity types response model.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/extract_graph_prompt.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 111
- **Mô tả module**: Entity Extraction prompt generator module.
- **Imports nổi bật**: pathlib (Path), graphrag_llm.tokenizer (Tokenizer), graphrag.prompt_tune.template.extract_graph (EXAMPLE_EXTRACTION_TEMPLATE, GRAPH_EXTRACTION_JSON_PROMPT, GRAPH_EXTRACTION_PROMPT, UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE, UNTYPED_GRAPH_EXTRACTION_PROMPT), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `create_extract_graph_prompt(entity_types, docs, examples, language, max_token_count, tokenizer, json_mode, output_path, min_examples_required) -> str`
    - Mục đích: Create a prompt for entity extraction.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/language.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 35
- **Mô tả module**: Language detection for GraphRAG prompts.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag.prompt_tune.prompt.language (DETECT_LANGUAGE_PROMPT)
- **Hàm top-level**:
  - `detect_language(model, docs) -> str`
    - Mục đích: Detect input language to use for GraphRAG prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/generator/persona.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 35
- **Mô tả module**: Persona generating module for fine-tuning GraphRAG prompts.
- **Imports nổi bật**: typing (TYPE_CHECKING), graphrag.prompt_tune.defaults (DEFAULT_TASK), graphrag.prompt_tune.prompt.persona (GENERATE_PERSONA_PROMPT)
- **Hàm top-level**:
  - `generate_persona(model, domain, task) -> str`
    - Mục đích: Generate an LLM persona to use for GraphRAG prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompt_tune/loader`

- Số file: **2**

#### File: `packages/graphrag/graphrag/prompt_tune/loader/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Fine-tuning config and data loader module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/loader/input.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 108
- **Mô tả module**: Input loading module.
- **Imports nổi bật**: dataclasses, logging, typing (Any), numpy, pandas, graphrag_chunking.chunker_factory (create_chunker), graphrag_input (create_input_reader), graphrag_llm.embedding (create_embedding), graphrag_storage (create_storage), graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.operations.embed_text.run_embed_text (run_embed_text)
- **Hàm top-level**:
  - `_sample_chunks_from_embeddings(text_chunks, embeddings, k) -> pd.DataFrame`
    - Mục đích: Sample text chunks from embeddings.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_docs_in_chunks(config, select_method, limit, logger, n_subset_max, k) -> list[str]`
    - Mục đích: Load docs into chunks for generating prompts.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py, tests/unit/prompt_tune/test_load_docs_in_chunks.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompt_tune/prompt`

- Số file: **8**

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Persona, entity type, relationships and domain generation prompts module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/community_report_rating.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 133
- **Mô tả module**: Fine tuning prompts for Community Reports Rating.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/community_reporter_role.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 21
- **Mô tả module**: Fine-tuning prompts for community reporter role generation.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/domain.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 13
- **Mô tả module**: Fine-tuning prompts for domain generation.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/entity_relationship.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 356
- **Mô tả module**: Fine-tuning prompts for entity relationship generation.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/entity_types.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 90
- **Mô tả module**: Fine-tuning prompts for entity types generation.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/language.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 13
- **Mô tả module**: Fine-tuning prompts for language detection.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/prompt/persona.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 14
- **Mô tả module**: Fine-tuning prompts for persona generation.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompt_tune/template`

- Số file: **4**

#### File: `packages/graphrag/graphrag/prompt_tune/template/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Fine-tuning prompts for entity extraction, entity summarization, and community report summarization.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/template/community_report_summarization.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 106
- **Mô tả module**: Fine-tuning prompts for community report summarization.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/template/entity_summarization.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 23
- **Mô tả module**: Fine-tuning prompts for entity summarization.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompt_tune/template/extract_graph.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 142
- **Mô tả module**: Fine-tuning prompts for entity extraction.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompts`

- Số file: **1**

#### File: `packages/graphrag/graphrag/prompts/__init__.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 5
- **Mô tả module**: All prompts for the GraphRAG system.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompts/index`

- Số file: **6**

#### File: `packages/graphrag/graphrag/prompts/index/__init__.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 5
- **Mô tả module**: All prompts for the indexing engine.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/index/community_report.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 154
- **Mô tả module**: A file containing prompts definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/index/community_report_text_units.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 96
- **Mô tả module**: A file containing prompts definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/index/extract_claims.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 62
- **Mô tả module**: A file containing prompts definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/index/extract_graph.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 130
- **Mô tả module**: A file containing prompts definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/index/summarize_descriptions.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 21
- **Mô tả module**: A file containing prompts definition.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/prompts/query`

- Số file: **8**

#### File: `packages/graphrag/graphrag/prompts/query/__init__.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 5
- **Mô tả module**: All prompts for the query engine.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/basic_search_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 74
- **Mô tả module**: Basic Search prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/drift_search_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 168
- **Mô tả module**: DRIFT Search prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/global_search_knowledge_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 10
- **Mô tả module**: Global Search system prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/global_search_map_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 86
- **Mô tả module**: System prompts for global search.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/global_search_reduce_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 86
- **Mô tả module**: Global Search system prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/local_search_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 70
- **Mô tả module**: Local search system prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/prompts/query/question_gen_system_prompt.py`
- **Loại**: python
- **Vai trò**: Template prompt dùng cho extraction/summarization/query.
- **Số dòng**: 29
- **Mô tả module**: Question Generation system prompts.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: The query engine package root.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/factory.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 276
- **Mô tả module**: Query Factory methods to support CLI.
- **Imports nổi bật**: graphrag_llm.completion (create_completion), graphrag_llm.embedding (create_embedding), graphrag_vectors (VectorStore), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.data_model.text_unit (TextUnit), graphrag.query.context_builder.entity_extraction (EntityVectorStoreKey)
- **Hàm top-level**:
  - `get_local_search_engine(config, reports, text_units, entities, relationships, covariates, response_type, description_embedding_store, system_prompt, callbacks) -> LocalSearch`
    - Mục đích: Create a local search engine based on data + configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_global_search_engine(config, reports, entities, communities, response_type, dynamic_community_selection, map_system_prompt, reduce_system_prompt, general_knowledge_inclusion_prompt, callbacks) -> GlobalSearch`
    - Mục đích: Create a global search engine based on data + configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_drift_search_engine(config, reports, text_units, entities, relationships, description_embedding_store, response_type, local_system_prompt, reduce_system_prompt, callbacks) -> DRIFTSearch`
    - Mục đích: Create a local search engine based on data + configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_basic_search_engine(text_units, text_unit_embeddings, config, response_type, system_prompt, callbacks) -> BasicSearch`
    - Mục đích: Create a basic search engine based on data + configuration.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/indexer_adapters.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 226
- **Mô tả module**: Indexing-Engine to Query Read Adapters.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING, cast), pandas, graphrag_vectors (VectorStore), graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.data_model.text_unit (TextUnit), graphrag.query.input.loaders.dfs (read_communities, read_community_reports, read_covariates, read_entities, read_relationships, read_text_units)
- **Hàm top-level**:
  - `read_indexer_text_units(final_text_units) -> list[TextUnit]`
    - Mục đích: Read in the Text Units from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_covariates(final_covariates) -> list[Covariate]`
    - Mục đích: Read in the Claims from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_relationships(final_relationships) -> list[Relationship]`
    - Mục đích: Read in the Relationships from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_reports(final_community_reports, final_communities, community_level, dynamic_community_selection) -> list[CommunityReport]`
    - Mục đích: Read in the Community Reports from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_report_embeddings(community_reports, embeddings_store)`
    - Mục đích: Read in the Community Reports from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_entities(entities, communities, community_level) -> list[Entity]`
    - Mục đích: Read in the Entities from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_indexer_communities(final_communities, final_community_reports) -> list[Community]`
    - Mục đích: Read in the Communities from the raw indexing outputs.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `embed_community_reports(reports_df, embedder, source_col, embedding_col) -> pd.DataFrame`
    - Mục đích: Embed a source column of the reports dataframe using the given embedder.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_filter_under_community_level(df, community_level) -> pd.DataFrame`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/context_builder`

- Số file: **10**

#### File: `packages/graphrag/graphrag/query/context_builder/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: Functions to build context for system prompt to generate responses for a user query.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/builders.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 76
- **Mô tả module**: Base classes for global and local context builders.
- **Imports nổi bật**: abc (ABC, abstractmethod), dataclasses (dataclass), pandas, graphrag.query.context_builder.conversation_history (ConversationHistory)
- **Class top-level**:
  - `ContextBuilderResult`
    - Mục đích: A class to hold the results of the build_context.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/question_gen/local_gen.py, packages/graphrag/graphrag/query/structured_search/basic_search/basic_context.py, packages/graphrag/graphrag/query/structured_search/global_search/community_context.py, packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
  - `GlobalContextBuilder`
    - Mục đích: Base class for global-search context builders.
    - Methods chính: build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/question_gen/base.py, packages/graphrag/graphrag/query/structured_search/base.py, packages/graphrag/graphrag/query/structured_search/global_search/community_context.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py
  - `LocalContextBuilder`
    - Mục đích: Base class for local-search context builders.
    - Methods chính: build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/question_gen/base.py, packages/graphrag/graphrag/query/question_gen/local_gen.py, packages/graphrag/graphrag/query/structured_search/base.py, packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py, packages/graphrag/graphrag/query/structured_search/local_search/search.py
  - `DRIFTContextBuilder`
    - Mục đích: Base class for DRIFT-search context builders.
    - Methods chính: build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/base.py, packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py
  - `BasicContextBuilder`
    - Mục đích: Base class for basic-search context builders.
    - Methods chính: build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/base.py, packages/graphrag/graphrag/query/structured_search/basic_search/basic_context.py, packages/graphrag/graphrag/query/structured_search/basic_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/community_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 265
- **Mô tả module**: Community Context.
- **Imports nổi bật**: logging, random, typing (Any, cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.entity (Entity), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `build_community_context(community_reports, entities, tokenizer, use_community_summary, column_delimiter, shuffle_data, include_community_rank, min_community_rank, community_rank_name, include_community_weight, community_weight_name, normalize_community_weight, max_context_tokens, single_batch, context_name, random_state) -> tuple[str | list[str], dict[str, pd.DataFrame]]`
    - Mục đích: Prepare community report data table as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/global_search/community_context.py, packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_compute_community_weights(community_reports, entities, weight_attribute, normalize) -> list[CommunityReport]`
    - Mục đích: Calculate a community's weight as count of text units associated with entities within the community.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_rank_report_context(report_df, weight_column, rank_column) -> pd.DataFrame`
    - Mục đích: Sort report context by community weight and rank if exist.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_convert_report_context_to_df(context_records, header, weight_column, rank_column) -> pd.DataFrame`
    - Mục đích: Convert report context records to pandas dataframe and sort by weight and rank if exist.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/conversation_history.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 214
- **Mô tả module**: Classes for storing and managing conversation history.
- **Imports nổi bật**: dataclasses (dataclass), enum (Enum), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Class top-level**:
  - `ConversationRole`
    - Mục đích: Enum for conversation roles.
    - Methods chính: from_string, __str__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ConversationTurn`
    - Mục đích: Data class for storing a single conversation turn.
    - Methods chính: __str__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `QATurn`
    - Mục đích: Data class for storing a QA turn.
    - Methods chính: get_answer_text, __str__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ConversationHistory`
    - Mục đích: Class for storing a conversation history.
    - Methods chính: __init__, from_list, add_turn, to_qa_turns, get_user_turns, build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/builders.py, packages/graphrag/graphrag/query/question_gen/local_gen.py, packages/graphrag/graphrag/query/structured_search/base.py, packages/graphrag/graphrag/query/structured_search/basic_search/basic_context.py, packages/graphrag/graphrag/query/structured_search/basic_search/search.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/dynamic_community_selection.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 177
- **Mô tả module**: Algorithm to dynamically select relevant communities with respect to a query.
- **Imports nổi bật**: asyncio, logging, collections (Counter), copy (deepcopy), time (time), typing (TYPE_CHECKING, Any), graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.query.context_builder.rate_prompt (RATE_QUERY), graphrag.query.context_builder.rate_relevancy (rate_relevancy)
- **Class top-level**:
  - `DynamicCommunitySelection`
    - Mục đích: Dynamic community selection to select community reports that are relevant to the query.
    - Methods chính: __init__, select
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/global_search/community_context.py, tests/unit/query/context_builder/dynamic_community_selection.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/entity_extraction.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 126
- **Mô tả module**: Orchestration Context Builders.
- **Imports nổi bật**: enum (Enum), typing (TYPE_CHECKING), graphrag_vectors (VectorStore), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.query.input.retrieval.entities (get_entity_by_id, get_entity_by_key, get_entity_by_name)
- **Hàm top-level**:
  - `map_query_to_entities(query, text_embedding_vectorstore, text_embedder, all_entities_dict, embedding_vectorstore_key, include_entity_names, exclude_entity_names, k, oversample_scaler) -> list[Entity]`
    - Mục đích: Extract entities that match a given query using semantic similarity of text embeddings of query and entity descriptions.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py, tests/unit/query/context_builder/test_entity_extraction.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `find_nearest_neighbors_by_entity_rank(entity_name, all_entities, all_relationships, exclude_entity_names, k) -> list[Entity]`
    - Mục đích: Retrieve entities that have direct connections with the target entity, sorted by entity rank.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `EntityVectorStoreKey`
    - Mục đích: Keys used as ids in the entity embedding vectorstores.
    - Methods chính: from_string
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py, tests/unit/query/context_builder/test_entity_extraction.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/local_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 358
- **Mô tả module**: Local Context Builder.
- **Imports nổi bật**: collections (defaultdict), typing (Any, cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.query.input.retrieval.covariates (get_candidate_covariates, to_covariate_dataframe), graphrag.query.input.retrieval.entities (to_entity_dataframe), graphrag.query.input.retrieval.relationships (get_candidate_relationships, get_entities_from_relationships, get_in_network_relationships, get_out_network_relationships, to_relationship_dataframe), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `build_entity_context(selected_entities, tokenizer, max_context_tokens, include_entity_rank, rank_description, column_delimiter, context_name) -> tuple[str, pd.DataFrame]`
    - Mục đích: Prepare entity data table as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `build_covariates_context(selected_entities, covariates, tokenizer, max_context_tokens, column_delimiter, context_name) -> tuple[str, pd.DataFrame]`
    - Mục đích: Prepare covariate data tables as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `build_relationship_context(selected_entities, relationships, tokenizer, include_relationship_weight, max_context_tokens, top_k_relationships, relationship_ranking_attribute, column_delimiter, context_name) -> tuple[str, pd.DataFrame]`
    - Mục đích: Prepare relationship data tables as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_filter_relationships(selected_entities, relationships, top_k_relationships, relationship_ranking_attribute) -> list[Relationship]`
    - Mục đích: Filter and sort relationships based on a set of selected entities and a ranking attribute.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_candidate_context(selected_entities, entities, relationships, covariates, include_entity_rank, entity_rank_description, include_relationship_weight) -> dict[str, pd.DataFrame]`
    - Mục đích: Prepare entity, relationship, and covariate data tables as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/rate_prompt.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 24
- **Mô tả module**: Global search with dynamic community selection prompt.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/rate_relevancy.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 87
- **Mô tả module**: Algorithm to rate the relevancy between a query and description text.
- **Imports nổi bật**: asyncio, logging, contextlib (nullcontext), typing (TYPE_CHECKING, Any), numpy, graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder, gather_completion_response_async), graphrag.query.context_builder.rate_prompt (RATE_QUERY), graphrag.query.llm.text_utils (try_parse_json_object)
- **Hàm top-level**:
  - `rate_relevancy(query, description, model, tokenizer, rate_query, num_repeats, semaphore, **model_params) -> dict[str, Any]`
    - Mục đích: Rate the relevancy between the query and description on a scale of 0 to 10.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/dynamic_community_selection.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/context_builder/source_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 101
- **Mô tả module**: Context Build utility methods.
- **Imports nổi bật**: random, typing (Any, cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.relationship (Relationship), graphrag.data_model.text_unit (TextUnit), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `build_text_unit_context(text_units, tokenizer, column_delimiter, shuffle_data, max_context_tokens, context_name, random_state) -> tuple[str, dict[str, pd.DataFrame]]`
    - Mục đích: Prepare text-unit data table as context data for system prompt.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `count_relationships(entity_relationships, text_unit) -> int`
    - Mục đích: Count the number of relationships of the selected entity that are associated with the text unit.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/input`

- Số file: **1**

#### File: `packages/graphrag/graphrag/query/input/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: GraphRAG Orchestration Inputs.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/input/loaders`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/input/loaders/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: GraphRAG Orchestartion Input Loaders.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/loaders/dfs.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 258
- **Mô tả module**: Load data from dataframes into collections of data objects.
- **Imports nổi bật**: pandas, graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.data_model.text_unit (TextUnit), graphrag.query.input.loaders.utils (to_list, to_optional_dict, to_optional_float, to_optional_int, to_optional_list, to_optional_str, to_str)
- **Hàm top-level**:
  - `_prepare_records(df) -> list[dict]`
    - Mục đích: Reset index and convert the DataFrame to a list of dictionaries.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_entities(df, id_col, short_id_col, title_col, type_col, description_col, name_embedding_col, description_embedding_col, community_col, text_unit_ids_col, rank_col, attributes_cols) -> list[Entity]`
    - Mục đích: Read entities from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_relationships(df, id_col, short_id_col, source_col, target_col, description_col, rank_col, description_embedding_col, weight_col, text_unit_ids_col, attributes_cols) -> list[Relationship]`
    - Mục đích: Read relationships from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_covariates(df, id_col, short_id_col, subject_col, covariate_type_col, text_unit_ids_col, attributes_cols) -> list[Covariate]`
    - Mục đích: Read covariates from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_communities(df, id_col, short_id_col, title_col, level_col, entities_col, relationships_col, text_units_col, covariates_col, parent_col, children_col, attributes_cols) -> list[Community]`
    - Mục đích: Read communities from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_community_reports(df, id_col, short_id_col, title_col, community_col, summary_col, content_col, rank_col, attributes_cols) -> list[CommunityReport]`
    - Mục đích: Read community reports from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `read_text_units(df, id_col, text_col, entities_col, relationships_col, covariates_col, tokens_col, document_id_col, attributes_cols) -> list[TextUnit]`
    - Mục đích: Read text units from a dataframe using pre-converted records.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/indexer_adapters.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/loaders/utils.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 188
- **Mô tả module**: Data load utils.
- **Imports nổi bật**: collections.abc (Mapping), typing (Any), numpy
- **Hàm top-level**:
  - `_get_value(data, column_name, required) -> Any`
    - Mục đích: Retrieve a column value from data.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_str(data, column_name) -> str`
    - Mục đích: Convert and validate a value to a string.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_optional_str(data, column_name) -> str | None`
    - Mục đích: Convert and validate a value to an optional string.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_list(data, column_name, item_type) -> list`
    - Mục đích: Convert and validate a value to a list.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/graphrag_vectors/lancedb.py, packages/graphrag/graphrag/query/context_builder/community_context.py, packages/graphrag/graphrag/query/indexer_adapters.py, packages/graphrag/graphrag/query/input/loaders/dfs.py, packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_optional_list(data, column_name, item_type) -> list | None`
    - Mục đích: Convert and validate a value to an optional list.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_int(data, column_name) -> int`
    - Mục đích: Convert and validate a value to an int.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_optional_int(data, column_name) -> int | None`
    - Mục đích: Convert and validate a value to an optional int.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_float(data, column_name) -> float`
    - Mục đích: Convert and validate a value to a float.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_optional_float(data, column_name) -> float | None`
    - Mục đích: Convert and validate a value to an optional float.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_dict(data, column_name, key_type, value_type) -> dict`
    - Mục đích: Convert and validate a value to a dict.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/parquet_table.py, packages/graphrag-vectors/example_notebooks/azure_ai_search.ipynb, packages/graphrag-vectors/example_notebooks/cosmosdb.ipynb, packages/graphrag-vectors/example_notebooks/lancedb.ipynb, packages/graphrag/graphrag/data_model/row_transformers.py, packages/graphrag/graphrag/index/operations/summarize_communities/graph_context/context_builder.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_optional_dict(data, column_name, key_type, value_type) -> dict | None`
    - Mục đích: Convert and validate a value to an optional dict.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/input/loaders/dfs.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/input/retrieval`

- Số file: **6**

#### File: `packages/graphrag/graphrag/query/input/retrieval/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: GraphRAG Orchestration Input Retrieval.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/retrieval/community_reports.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 76
- **Mô tả module**: Util functions to retrieve community reports from a collection.
- **Imports nổi bật**: typing (Any, cast), pandas, graphrag.data_model.community_report (CommunityReport), graphrag.data_model.entity (Entity)
- **Hàm top-level**:
  - `get_candidate_communities(selected_entities, community_reports, include_community_rank, use_community_summary) -> pd.DataFrame`
    - Mục đích: Get all communities that are related to selected entities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_community_report_dataframe(reports, include_community_rank, use_community_summary) -> pd.DataFrame`
    - Mục đích: Convert a list of communities to a pandas dataframe.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/retrieval/covariates.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 54
- **Mô tả module**: Util functions to retrieve covariates from a collection.
- **Imports nổi bật**: typing (Any, cast), pandas, graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity)
- **Hàm top-level**:
  - `get_candidate_covariates(selected_entities, covariates) -> list[Covariate]`
    - Mục đích: Get all covariates that are related to selected entities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_covariate_dataframe(covariates) -> pd.DataFrame`
    - Mục đích: Convert a list of covariates to a pandas dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/retrieval/entities.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 103
- **Mô tả module**: Util functions to get entities from a collection.
- **Imports nổi bật**: uuid, collections.abc (Iterable), typing (Any, cast), pandas, graphrag.data_model.entity (Entity)
- **Hàm top-level**:
  - `get_entity_by_id(entities, value) -> Entity | None`
    - Mục đích: Get entity by id.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/entity_extraction.py, tests/unit/query/input/retrieval/test_entities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_entity_by_key(entities, key, value) -> Entity | None`
    - Mục đích: Get entity by key.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/entity_extraction.py, tests/unit/query/input/retrieval/test_entities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_entity_by_name(entities, entity_name) -> list[Entity]`
    - Mục đích: Get entities by name.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/entity_extraction.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_entity_by_attribute(entities, attribute_name, attribute_value) -> list[Entity]`
    - Mục đích: Get entities by attribute.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_entity_dataframe(entities, include_entity_rank, rank_description) -> pd.DataFrame`
    - Mục đích: Convert a list of entities to a pandas dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `is_valid_uuid(value) -> bool`
    - Mục đích: Determine if a string is a valid UUID.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/retrieval/relationships.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 140
- **Mô tả module**: Util functions to retrieve relationships from a collection.
- **Imports nổi bật**: typing (Any, cast), pandas, graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship)
- **Hàm top-level**:
  - `get_in_network_relationships(selected_entities, relationships, ranking_attribute) -> list[Relationship]`
    - Mục đích: Get all directed relationships between selected entities, sorted by ranking_attribute.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_out_network_relationships(selected_entities, relationships, ranking_attribute) -> list[Relationship]`
    - Mục đích: Get relationships from selected entities to other entities that are not within the selected entities, sorted by ranking_attribute.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_candidate_relationships(selected_entities, relationships) -> list[Relationship]`
    - Mục đích: Get all relationships that are associated with the selected entities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `get_entities_from_relationships(relationships, entities) -> list[Entity]`
    - Mục đích: Get all entities that are associated with the selected relationships.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `sort_relationships_by_rank(relationships, ranking_attribute) -> list[Relationship]`
    - Mục đích: Sort relationships by a ranking_attribute.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_relationship_dataframe(relationships, include_relationship_weight) -> pd.DataFrame`
    - Mục đích: Convert a list of relationships to a pandas dataframe.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/local_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/input/retrieval/text_units.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 54
- **Mô tả module**: Util functions to retrieve text units from a collection.
- **Imports nổi bật**: typing (Any, cast), pandas, graphrag.data_model.entity (Entity), graphrag.data_model.text_unit (TextUnit)
- **Hàm top-level**:
  - `get_candidate_text_units(selected_entities, text_units) -> pd.DataFrame`
    - Mục đích: Get all text units that are associated to selected entities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `to_text_unit_dataframe(text_units) -> pd.DataFrame`
    - Mục đích: Convert a list of text units to a pandas dataframe.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/llm`

- Số file: **2**

#### File: `packages/graphrag/graphrag/query/llm/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: Orchestration LLM utilities.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/llm/text_utils.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 104
- **Mô tả module**: Text Utilities for LLM.
- **Imports nổi bật**: json, logging, re, collections.abc (Iterator), itertools (islice), graphrag_llm.tokenizer (Tokenizer), json_repair (repair_json), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `batched(iterable, n)`
    - Mục đích: Batch data into tuples of length n. The last batch may be shorter.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `chunk_text(text, max_tokens, tokenizer)`
    - Mục đích: Chunk text by token length.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-chunking/graphrag_chunking/token_chunker.py, packages/graphrag/graphrag/index/text_splitting/text_splitting.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `try_parse_json_object(input, verbose) -> tuple[str, dict]`
    - Mục đích: JSON cleaning and formatting utilities.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/context_builder/rate_relevancy.py, packages/graphrag/graphrag/query/structured_search/drift_search/action.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/question_gen`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/question_gen/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: Question Generation Module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/question_gen/base.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 68
- **Mô tả module**: Base classes for generating questions based on previously asked questions and most recent context data.
- **Imports nổi bật**: abc (ABC, abstractmethod), dataclasses (dataclass), typing (TYPE_CHECKING, Any), graphrag_llm.tokenizer (Tokenizer), graphrag.query.context_builder.builders (GlobalContextBuilder, LocalContextBuilder)
- **Class top-level**:
  - `QuestionResult`
    - Mục đích: A Structured Question Result.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/question_gen/local_gen.py
  - `BaseQuestionGen`
    - Mục đích: The Base Question Gen implementation.
    - Methods chính: __init__, generate, agenerate
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/question_gen/local_gen.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/question_gen/local_gen.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 238
- **Mô tả module**: Local question generation.
- **Imports nổi bật**: logging, time, typing (TYPE_CHECKING, Any, cast), graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder), graphrag.callbacks.llm_callbacks (BaseLLMCallback), graphrag.prompts.query.question_gen_system_prompt (QUESTION_SYSTEM_PROMPT), graphrag.query.context_builder.builders (ContextBuilderResult, LocalContextBuilder), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.query.question_gen.base (BaseQuestionGen, QuestionResult)
- **Class top-level**:
  - `LocalQuestionGen`
    - Mục đích: Search orchestration for global search mode.
    - Methods chính: __init__, agenerate, generate
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/structured_search`

- Số file: **2**

#### File: `packages/graphrag/graphrag/query/structured_search/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: Structured Search package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/base.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 94
- **Mô tả module**: Base classes for search algos.
- **Imports nổi bật**: abc (ABC, abstractmethod), collections.abc (AsyncGenerator), dataclasses (dataclass), typing (TYPE_CHECKING, Any, Generic, TypeVar), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag.query.context_builder.builders (BasicContextBuilder, DRIFTContextBuilder, GlobalContextBuilder, LocalContextBuilder), graphrag.query.context_builder.conversation_history (ConversationHistory)
- **Class top-level**:
  - `SearchResult`
    - Mục đích: A Structured Search Result.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/callbacks/noop_query_callbacks.py, packages/graphrag/graphrag/callbacks/query_callbacks.py, packages/graphrag/graphrag/query/structured_search/basic_search/search.py, packages/graphrag/graphrag/query/structured_search/drift_search/primer.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py
  - `BaseSearch`
    - Mục đích: The Base Search implementation.
    - Methods chính: __init__, search, stream_search
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/basic_search/search.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/global_search/search.py, packages/graphrag/graphrag/query/structured_search/local_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/structured_search/basic_search`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/structured_search/basic_search/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: The BasicSearch package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/basic_search/basic_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 110
- **Mô tả module**: Basic Context Builder implementation.
- **Imports nổi bật**: logging, typing (TYPE_CHECKING, cast), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag_vectors (VectorStore), graphrag.data_model.text_unit (TextUnit), graphrag.query.context_builder.builders (BasicContextBuilder, ContextBuilderResult), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Class top-level**:
  - `BasicSearchContext`
    - Mục đích: Class representing the Basic Search Context Builder.
    - Methods chính: __init__, build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/basic_search/search.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 183
- **Mô tả module**: BasicSearch implementation.
- **Imports nổi bật**: logging, time, collections.abc (AsyncGenerator, AsyncIterator), typing (TYPE_CHECKING, Any), graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.prompts.query.basic_search_system_prompt (BASIC_SEARCH_SYSTEM_PROMPT), graphrag.query.context_builder.builders (BasicContextBuilder), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.query.structured_search.base (BaseSearch, SearchResult)
- **Class top-level**:
  - `BasicSearch`
    - Mục đích: Search orchestration for basic search mode.
    - Methods chính: __init__, search, stream_search
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/basic_search/__init__.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/structured_search/drift_search`

- Số file: **6**

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: DriftSearch module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/action.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 246
- **Mô tả module**: DRIFT Search Query State.
- **Imports nổi bật**: json, logging, typing (Any), graphrag.query.llm.text_utils (try_parse_json_object)
- **Class top-level**:
  - `DriftAction`
    - Mục đích: Represent an action containing a query, answer, score, and follow-up actions.
    - Methods chính: __init__, is_complete, search, compute_score, serialize, deserialize, from_primer_response, __hash__, __eq__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/drift_search/state.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 230
- **Mô tả module**: DRIFT Context Builder implementation.
- **Imports nổi bật**: logging, dataclasses (asdict), typing (TYPE_CHECKING, Any), numpy, pandas, graphrag_llm.tokenizer (Tokenizer), graphrag_vectors (VectorStore), graphrag.config.models.drift_search_config (DRIFTSearchConfig), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship)
- **Class top-level**:
  - `DRIFTSearchContextBuilder`
    - Mục đích: Class representing the DRIFT Search Context Builder.
    - Methods chính: __init__, init_local_context_builder, convert_reports_to_df, check_query_doc_encodings, build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/primer.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 227
- **Mô tả module**: Primer for DRIFT search.
- **Imports nổi bật**: logging, secrets, time, typing (TYPE_CHECKING), numpy, pandas, graphrag_llm.tokenizer (Tokenizer), pydantic (BaseModel, Field), tqdm.asyncio (tqdm_asyncio), graphrag.config.models.drift_search_config (DRIFTSearchConfig), graphrag.data_model.community_report (CommunityReport), graphrag.prompts.query.drift_search_system_prompt (DRIFT_PRIMER_PROMPT)
- **Class top-level**:
  - `PrimerResponse`
    - Mục đích: Response model for the primer.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `PrimerQueryProcessor`
    - Mục đích: Process the query by expanding it using community reports and generate follow-up actions.
    - Methods chính: __init__, expand_query, __call__
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py
  - `DRIFTPrimer`
    - Mục đích: Perform initial query decomposition using global guidance from information in community reports.
    - Methods chính: __init__, decompose_query, search, split_reports
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/drift_search/action.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/search.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 465
- **Mô tả module**: DRIFT Search implementation.
- **Imports nổi bật**: logging, time, collections.abc (AsyncGenerator, AsyncIterator), typing (TYPE_CHECKING, Any), graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder, gather_completion_response_async), tqdm.asyncio (tqdm_asyncio), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.query.context_builder.entity_extraction (EntityVectorStoreKey), graphrag.query.structured_search.base (BaseSearch, SearchResult), graphrag.query.structured_search.drift_search.action (DriftAction)
- **Class top-level**:
  - `DRIFTSearch`
    - Mục đích: Class representing a DRIFT Search.
    - Methods chính: __init__, init_local_search, _process_primer_results, _search_step, search, stream_search, _reduce_response, _reduce_response_streaming
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/drift_search/state.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 151
- **Mô tả module**: Manage the state of the DRIFT query, including a graph of actions.
- **Imports nổi bật**: logging, random, collections.abc (Callable), typing (Any), networkx, graphrag.query.structured_search.drift_search.action (DriftAction)
- **Class top-level**:
  - `QueryState`
    - Mục đích: Manage the state of the query, including a graph of actions.
    - Methods chính: __init__, add_action, relate_actions, add_all_follow_ups, find_incomplete_actions, rank_incomplete_actions, serialize, deserialize, action_token_ct
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/structured_search/drift_search/search.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/structured_search/global_search`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/structured_search/global_search/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: GlobalSearch module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/global_search/community_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 146
- **Mô tả module**: Contains algorithms to build context data for global search prompt.
- **Imports nổi bật**: typing (Any), graphrag_llm.tokenizer (Tokenizer), graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.entity (Entity), graphrag.query.context_builder.builders (ContextBuilderResult), graphrag.query.context_builder.community_context (build_community_context), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.query.context_builder.dynamic_community_selection (DynamicCommunitySelection), graphrag.query.structured_search.base (GlobalContextBuilder), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Class top-level**:
  - `GlobalCommunityContext`
    - Mục đích: GlobalSearch community context builder.
    - Methods chính: __init__, build_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/global_search/search.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 522
- **Mô tả module**: The GlobalSearch Implementation.
- **Imports nổi bật**: asyncio, json, logging, time, collections.abc (AsyncGenerator, AsyncIterator), dataclasses (dataclass), typing (TYPE_CHECKING, Any), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder, gather_completion_response_async), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.prompts.query.global_search_knowledge_system_prompt (GENERAL_KNOWLEDGE_INSTRUCTION)
- **Class top-level**:
  - `GlobalSearchResult`
    - Mục đích: A GlobalSearch result.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `GlobalSearch`
    - Mục đích: Search orchestration for global search mode.
    - Methods chính: __init__, stream_search, search, _map_response_single_batch, _parse_search_response, _reduce_response, _stream_reduce_response
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/global_search/__init__.py, packages/graphrag/graphrag/query/structured_search/global_search/community_context.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/query/structured_search/local_search`

- Số file: **3**

#### File: `packages/graphrag/graphrag/query/structured_search/local_search/__init__.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 5
- **Mô tả module**: The LocalSearch package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/local_search/mixed_context.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 492
- **Mô tả module**: Algorithms to build context data for local search prompt.
- **Imports nổi bật**: logging, copy (deepcopy), typing (TYPE_CHECKING, Any), pandas, graphrag_llm.tokenizer (Tokenizer), graphrag_vectors (VectorStore), graphrag.data_model.community_report (CommunityReport), graphrag.data_model.covariate (Covariate), graphrag.data_model.entity (Entity), graphrag.data_model.relationship (Relationship), graphrag.data_model.text_unit (TextUnit), graphrag.query.context_builder.builders (ContextBuilderResult)
- **Class top-level**:
  - `LocalSearchMixedContext`
    - Mục đích: Build data context for local search prompt combining community reports and entity/relationship/covariate tables.
    - Methods chính: __init__, build_context, _build_community_context, _build_text_unit_context, _build_local_context
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/drift_search/drift_context.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/query/structured_search/local_search/search.py`
- **Loại**: python
- **Vai trò**: Engine truy vấn (local/global/drift/basic) trên chỉ mục đã index.
- **Số dòng**: 184
- **Mô tả module**: LocalSearch implementation.
- **Imports nổi bật**: logging, time, collections.abc (AsyncGenerator, AsyncIterator), typing (TYPE_CHECKING, Any), graphrag_llm.tokenizer (Tokenizer), graphrag_llm.utils (CompletionMessagesBuilder), graphrag.callbacks.query_callbacks (QueryCallbacks), graphrag.prompts.query.local_search_system_prompt (LOCAL_SEARCH_SYSTEM_PROMPT), graphrag.query.context_builder.builders (LocalContextBuilder), graphrag.query.context_builder.conversation_history (ConversationHistory), graphrag.query.structured_search.base (BaseSearch, SearchResult)
- **Class top-level**:
  - `LocalSearch`
    - Mục đích: Search orchestration for local search mode.
    - Methods chính: __init__, search, stream_search
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/query/factory.py, packages/graphrag/graphrag/query/structured_search/drift_search/search.py, packages/graphrag/graphrag/query/structured_search/local_search/__init__.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/tokenizer`

- Số file: **2**

#### File: `packages/graphrag/graphrag/tokenizer/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: GraphRAG tokenizer.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/tokenizer/get_tokenizer.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 49
- **Mô tả module**: Get Tokenizer.
- **Imports nổi bật**: graphrag_llm.config (ModelConfig, TokenizerConfig, TokenizerType), graphrag_llm.tokenizer (Tokenizer, create_tokenizer), graphrag.config.defaults (ENCODING_MODEL)
- **Hàm top-level**:
  - `get_tokenizer(model_config, encoding_model) -> Tokenizer`
    - Mục đích: Get the tokenizer for the given model configuration or fallback to a tiktoken based tokenizer.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/prompt_tune.py, packages/graphrag/graphrag/index/text_splitting/text_splitting.py, packages/graphrag/graphrag/index/workflows/create_base_text_units.py, packages/graphrag/graphrag/prompt_tune/generator/extract_graph_prompt.py, packages/graphrag/graphrag/query/context_builder/community_context.py, packages/graphrag/graphrag/query/context_builder/conversation_history.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `packages/graphrag/graphrag/utils`

- Số file: **3**

#### File: `packages/graphrag/graphrag/utils/__init__.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 5
- **Mô tả module**: Util functions for the GraphRAG package.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/utils/api.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 76
- **Mô tả module**: API functions for the GraphRAG module.
- **Imports nổi bật**: pathlib (Path), graphrag_vectors (VectorStore, VectorStoreConfig, create_vector_store)
- **Hàm top-level**:
  - `get_embedding_store(config, embedding_name) -> VectorStore`
    - Mục đích: Get the embedding store.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `reformat_context_data(context_data) -> dict`
    - Mục đích: Reformats context_data for all query responses.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_search_prompt(prompt_config) -> str | None`
    - Mục đích: Load the search prompt from disk if configured.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `truncate(text, max_length) -> str`
    - Mục đích: Truncate a string to a maximum length.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/csv_table.py, packages/graphrag-storage/graphrag_storage/tables/csv_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table.py, packages/graphrag-storage/graphrag_storage/tables/parquet_table_provider.py, packages/graphrag-storage/graphrag_storage/tables/table_provider.py, packages/graphrag/graphrag/api/query.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `packages/graphrag/graphrag/utils/cli.py`
- **Loại**: python
- **Vai trò**: Thành phần hạ tầng/phụ trợ trong hệ GraphRAG.
- **Số dòng**: 55
- **Mô tả module**: CLI functions for the GraphRAG module.
- **Imports nổi bật**: argparse, json, pathlib (Path)
- **Hàm top-level**:
  - `file_exist(path)`
    - Mục đích: Check for file existence.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `dir_exist(path)`
    - Mục đích: Check for directory existence.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `redact(config) -> str`
    - Mục đích: Sanitize secrets in a config object.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag/graphrag/api/query.py, packages/graphrag/graphrag/cli/index.py, packages/graphrag/graphrag/cli/prompt_tune.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

## 2) Nhóm thư mục: `scripts`

### Thư mục con: `scripts`

- Số file: **6**

#### File: `scripts/__init__.py`
- **Loại**: python
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 6
- **Mô tả module**: GraphRAG Scripts module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `scripts/copy_build_assets.py`
- **Loại**: python
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 26
- **Mô tả module**: Copy root build assets to package directories.
- **Imports nổi bật**: shutil, pathlib (Path)
- **Hàm top-level**:
  - `copy_build_assets()`
    - Mục đích: Copy root build assets to package build directories so files are included in pypi distributions.
    - Được tham chiếu bởi (xấp xỉ): pyproject.toml
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `scripts/semver-check.sh`
- **Loại**: shell
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 11
- **Lệnh chính (preview)**: changes=$(git diff --name-only origin/main) | has_change_doc=$(echo $changes | grep .semversioner/next-release) | has_impacting_changes=$(echo $changes | grep graphrag) | if [ "$has_impacting_changes" ] && [ -z "$has_change_doc" ]; then | echo "Check failed. Run 'uv run semversioner add-change' to update the next release version" | exit 1 | fi | echo "OK"
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `scripts/spellcheck.sh`
- **Loại**: shell
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 2
- **Lệnh chính (preview)**: npx --yes cspell -c cspell.config.yaml --no-progress lint .
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `scripts/start-azurite.sh`
- **Loại**: shell
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 2
- **Lệnh chính (preview)**: npx --yes azurite -L -l ./temp_azurite -d ./temp_azurite/debug.log
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `scripts/update_workspace_dependency_versions.py`
- **Loại**: python
- **Vai trò**: Script hỗ trợ phát triển, build hoặc kiểm tra chất lượng release.
- **Số dòng**: 59
- **Mô tả module**: Update workspace dependency versions.
- **Imports nổi bật**: os, re, subprocess, pathlib (Path)
- **Hàm top-level**:
  - `_get_version() -> str`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_get_package_paths() -> list[Path]`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `update_workspace_dependency_versions()`
    - Mục đích: Update dependency versions across workspace packages.
    - Được tham chiếu bởi (xấp xỉ): pyproject.toml
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

## 2) Nhóm thư mục: `tests`

### Thư mục con: `tests`

- Số file: **2**

#### File: `tests/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 6
- **Mô tả module**: Tests for the GraphRAG LLM module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/conftest.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 9
- **Hàm top-level**:
  - `pytest_addoption(parser)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/azure`

- Số file: **2**

#### File: `tests/fixtures/azure/config.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 14
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/azure/settings.yml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 36
- **Key cấu hình chính**: extract_claims, enabled, vector_store, type, url, api_key, container_name, input, storage, type, connection_string, container_name, base_dir, type, cache, type, connection_string, container_name, base_dir, output
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/azure/input`

- Số file: **2**

#### File: `tests/fixtures/azure/input/ABOUT.md`
- **Loại**: markdown
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Heading chính**: # About
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/azure/input/dulce.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/min-csv`

- Số file: **2**

#### File: `tests/fixtures/min-csv/config.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 106
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/min-csv/settings.yml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 37
- **Key cấu hình chính**: completion_models, default_completion_model, model_provider, api_key, api_base, api_version, model, azure_deployment_name, rate_limit, type, tokens_per_period, requests_per_period, embedding_models, default_embedding_model, model_provider, api_key, api_base, api_version, model, azure_deployment_name
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/min-csv/input`

- Số file: **2**

#### File: `tests/fixtures/min-csv/input/ABOUT.md`
- **Loại**: markdown
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Heading chính**: # About
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/min-csv/input/dulce.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/text`

- Số file: **2**

#### File: `tests/fixtures/text/config.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 112
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/text/settings.yml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 41
- **Key cấu hình chính**: completion_models, default_completion_model, model_provider, api_key, api_base, api_version, model, azure_deployment_name, rate_limit, type, tokens_per_period, requests_per_period, embedding_models, default_embedding_model, model_provider, api_key, api_base, api_version, model, azure_deployment_name
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/text/input`

- Số file: **2**

#### File: `tests/fixtures/text/input/ABOUT.md`
- **Loại**: markdown
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Heading chính**: # About
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/fixtures/text/input/dulce.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/fixtures/text/prompts`

- Số file: **1**

#### File: `tests/fixtures/text/prompts/community_report.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration`

- Số file: **1**

#### File: `tests/integration/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration/cache`

- Số file: **2**

#### File: `tests/integration/cache/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/cache/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 163
- **Mô tả module**: CacheFactory Tests.
- **Imports nổi bật**: sys, pytest, graphrag_cache (Cache, CacheConfig, CacheType, create_cache, register_cache), graphrag_cache.cache_factory (cache_factory), graphrag_cache.json_cache (JsonCache), graphrag_cache.memory_cache (MemoryCache), graphrag_cache.noop_cache (NoopCache), graphrag_storage (StorageConfig, StorageType, create_storage)
- **Hàm top-level**:
  - `test_create_noop_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_memory_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_file_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_blob_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_cosmosdb_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_and_create_custom_cache()`
    - Mục đích: Test registering and creating a custom cache type.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_unknown_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_class_directly_works()`
    - Mục đích: Test that registering a class directly works (CacheFactory() allows this).
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_factory.py, tests/integration/vector_stores/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration/language_model`

- Số file: **5**

#### File: `tests/integration/language_model/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/language_model/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 102
- **Mô tả module**: LLMFactory Tests.
- **Imports nổi bật**: typing (TYPE_CHECKING, Any, Unpack), graphrag_llm.completion (LLMCompletion, create_completion, register_completion), graphrag_llm.config (ModelConfig), graphrag_llm.embedding (LLMEmbedding, create_embedding, register_embedding)
- **Hàm top-level**:
  - `test_create_custom_chat_model()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_custom_embedding_llm()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/language_model/test_rate_limiter.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 350
- **Mô tả module**: Test LiteLLM Rate Limiter.
- **Imports nổi bật**: threading, time, math (ceil), queue (Queue), graphrag_llm.config (RateLimitConfig, RateLimitType), graphrag_llm.rate_limit (RateLimiter, create_rate_limiter), tests.integration.language_model.utils (assert_max_num_values_per_period, assert_stagger, bin_time_intervals)
- **Hàm top-level**:
  - `test_binning()`
    - Mục đích: Test binning timings into 1-second intervals.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_rpm()`
    - Mục đích: Test that the rate limiter enforces RPM limits.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_tpm()`
    - Mục đích: Test that the rate limiter enforces TPM limits.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_token_in_request_exceeds_tpm()`
    - Mục đích: Test that the rate limiter allows for requests that use more tokens than the TPM.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_rpm_and_tpm_with_rpm_as_limiting_factor()`
    - Mục đích: Test that the rate limiter enforces RPM and TPM limits.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_rpm_and_tpm_with_tpm_as_limiting_factor()`
    - Mục đích: Test that the rate limiter enforces TPM limits.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_run_rate_limiter(rate_limiter, input_queue, output_queue)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_rpm_threaded()`
    - Mục đích: Test that the rate limiter enforces RPM limits in a threaded environment.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_tpm_threaded()`
    - Mục đích: Test that the rate limiter enforces TPM limits in a threaded environment.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/language_model/test_retries.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 244
- **Mô tả module**: Test LiteLLM Retries.
- **Imports nổi bật**: time, typing (Any), httpx, litellm.exceptions, pytest, graphrag_llm.config (RetryConfig, RetryType), graphrag_llm.retry (create_retry)
- **Hàm top-level**:
  - `test_retries(config, max_retries, expected_time) -> None`
    - Mục đích: Test various retry strategies with various configurations.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_retries_async(config, max_retries, expected_time) -> None`
    - Mục đích: Test various retry strategies with various configurations.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_exponential_backoff_skipping_exceptions(config, exception, exception_args) -> None`
    - Mục đích: Test skipping retries for exceptions that should not cause a retry.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/language_model/utils.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 38
- **Mô tả module**: LiteLLM Test Utilities.
- **Hàm top-level**:
  - `bin_time_intervals(time_values, time_interval) -> list[list[float]]`
    - Mục đích: Bin values.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/language_model/test_rate_limiter.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_max_num_values_per_period(periods, max_values_per_period)`
    - Mục đích: Assert the number of values per period.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/language_model/test_rate_limiter.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_stagger(time_values, stagger)`
    - Mục đích: Assert stagger.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/language_model/test_rate_limiter.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration/logging`

- Số file: **3**

#### File: `tests/integration/logging/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 5
- **Mô tả module**: Tests for logger module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/logging/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 63
- **Mô tả module**: LoggerFactory Tests.
- **Imports nổi bật**: logging, pytest, graphrag.config.enums (ReportingType), graphrag.logger.blob_workflow_logger (BlobWorkflowLogger), graphrag.logger.factory (LoggerFactory)
- **Hàm top-level**:
  - `test_create_blob_logger()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_and_create_custom_logger()`
    - Mục đích: Test registering and creating a custom logger type.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_logger_types()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_unknown_logger()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/logging/test_standard_logging.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 136
- **Mô tả module**: Tests for standard logging functionality.
- **Imports nổi bật**: logging, os, tempfile, pathlib (Path), graphrag.logger.standard_logging (DEFAULT_LOG_FILENAME, init_loggers), tests.unit.config.utils (get_default_graphrag_config)
- **Hàm top-level**:
  - `test_standard_logging()`
    - Mục đích: Test that standard logging works.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_logger_hierarchy()`
    - Mục đích: Test that logger hierarchy works correctly.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_init_loggers_file_config()`
    - Mục đích: Test that init_loggers works with file configuration.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_init_loggers_file_verbose()`
    - Mục đích: Test that init_loggers works with verbose flag.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_init_loggers_custom_filename()`
    - Mục đích: Test that init_loggers works with custom filename.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration/storage`

- Số file: **5**

#### File: `tests/integration/storage/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/storage/test_blob_storage.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 90
- **Mô tả module**: Blob Storage Tests.
- **Imports nổi bật**: re, datetime (datetime), graphrag_storage.azure_blob_storage (AzureBlobStorage)
- **Hàm top-level**:
  - `test_find()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_cosmosdb_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_creation_date()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_cosmosdb_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_child()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_cosmosdb_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/storage/test_cosmosdb_storage.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 130
- **Mô tả module**: CosmosDB Storage Tests.
- **Imports nổi bật**: json, re, sys, datetime (datetime), pytest, graphrag_storage.azure_cosmos_storage (AzureCosmosStorage)
- **Hàm top-level**:
  - `test_find()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_child()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_clear()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/vector_stores/test_cosmosdb.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_creation_date()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_file_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/storage/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 151
- **Mô tả module**: StorageFactory Tests.
- **Imports nổi bật**: sys, pytest, graphrag_storage (Storage, StorageConfig, StorageType, create_storage, register_storage), graphrag_storage.azure_blob_storage (AzureBlobStorage), graphrag_storage.azure_cosmos_storage (AzureCosmosStorage), graphrag_storage.file_storage (FileStorage), graphrag_storage.memory_storage (MemoryStorage)
- **Hàm top-level**:
  - `test_create_blob_storage()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_cosmosdb_storage()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_file()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_memory_storage()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_and_create_custom_storage()`
    - Mục đích: Test registering and creating a custom storage type.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_unknown_storage()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_class_directly_works()`
    - Mục đích: Test that registering a class directly works (StorageFactory allows this).
    - Được tham chiếu bởi (xấp xỉ): tests/integration/cache/test_factory.py, tests/integration/vector_stores/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/storage/test_file_storage.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 60
- **Mô tả module**: Blob Storage Tests.
- **Imports nổi bật**: os, re, datetime (datetime), pathlib (Path), graphrag_storage.file_storage (FileStorage)
- **Hàm top-level**:
  - `test_find()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_cosmosdb_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_creation_date()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_cosmosdb_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_child()`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_blob_storage.py, tests/integration/storage/test_cosmosdb_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/integration/vector_stores`

- Số file: **5**

#### File: `tests/integration/vector_stores/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 5
- **Mô tả module**: Integration tests for vector store implementations.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/vector_stores/test_azure_ai_search.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 206
- **Mô tả module**: Integration tests for Azure AI Search vector store implementation.
- **Imports nổi bật**: os, unittest.mock (MagicMock, patch), pytest, graphrag_vectors (VectorStoreDocument), graphrag_vectors.azure_ai_search (AzureAISearchVectorStore)
- **Class top-level**:
  - `TestAzureAISearchVectorStore`
    - Mục đích: Test class for AzureAISearchVectorStore.
    - Methods chính: mock_search_client, mock_index_client, vector_store, vector_store_custom, sample_documents, test_vector_store_operations, test_empty_embedding, test_vector_store_customization
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/vector_stores/test_cosmosdb.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 147
- **Mô tả module**: Integration tests for CosmosDB vector store implementation.
- **Imports nổi bật**: sys, numpy, pytest, graphrag_vectors (VectorStoreDocument), graphrag_vectors.cosmosdb (CosmosDBVectorStore)
- **Hàm top-level**:
  - `test_vector_store_operations()`
    - Mục đích: Test basic vector store operations with CosmosDB.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/vector_stores/test_azure_ai_search.py, tests/integration/vector_stores/test_lancedb.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_clear()`
    - Mục đích: Test clearing the vector store.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/storage/test_cosmosdb_storage.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_vector_store_customization()`
    - Mục đích: Test vector store customization with CosmosDB.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/vector_stores/test_azure_ai_search.py, tests/integration/vector_stores/test_lancedb.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/vector_stores/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 172
- **Mô tả module**: VectorStoreFactory Tests.
- **Imports nổi bật**: pytest, graphrag_vectors (VectorStore, VectorStoreFactory, VectorStoreType), graphrag_vectors.azure_ai_search (AzureAISearchVectorStore), graphrag_vectors.cosmosdb (CosmosDBVectorStore), graphrag_vectors.lancedb (LanceDBVectorStore)
- **Hàm top-level**:
  - `test_create_lancedb_vector_store()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_azure_ai_search_vector_store()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_cosmosdb_vector_store()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_and_create_custom_vector_store()`
    - Mục đích: Test registering and creating a custom vector store type.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_unknown_vector_store()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_is_supported_type()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_register_class_directly_works()`
    - Mục đích: Test that registering a class directly works.
    - Được tham chiếu bởi (xấp xỉ): tests/integration/cache/test_factory.py, tests/integration/storage/test_factory.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/integration/vector_stores/test_lancedb.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 582
- **Mô tả module**: Integration tests for LanceDB vector store implementation.
- **Imports nổi bật**: shutil, tempfile, numpy, pytest, graphrag_vectors (VectorStoreDocument), graphrag_vectors.filtering (F), graphrag_vectors.lancedb (LanceDBVectorStore)
- **Class top-level**:
  - `TestLanceDBVectorStore`
    - Mục đích: Test class for TestLanceDBVectorStore.
    - Methods chính: sample_documents, sample_documents_with_metadata, store_with_fields, test_vector_store_operations, test_empty_collection, test_insert_and_count, test_load_documents, test_search_by_id, test_remove, test_update, test_update_sets_update_date, test_similarity_search_by_vector
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/notebook`

- Số file: **2**

#### File: `tests/notebook/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/notebook/test_notebooks.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 81
- **Imports nổi bật**: subprocess, dataclasses (dataclass), pathlib (Path), nbformat, pytest
- **Hàm top-level**:
  - `_notebook_run(filepath)`
    - Mục đích: Execute a notebook via nbconvert and collect output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `clear_cache()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_notebook(notebook_path)`
    - Được tham chiếu bởi (xấp xỉ): pyproject.toml
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `NotebookDetails`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/smoke`

- Số file: **2**

#### File: `tests/smoke/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/smoke/test_fixtures.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 273
- **Imports nổi bật**: asyncio, json, logging, os, shutil, subprocess, collections.abc (Callable), functools (wraps), pathlib (Path), typing (Any, ClassVar), unittest (mock), pandas
- **Hàm top-level**:
  - `_load_fixtures()`
    - Mục đích: Load all fixtures from the tests/data folder.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `pytest_generate_tests(metafunc)`
    - Mục đích: Generate tests for all test functions in this module.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `cleanup(skip)`
    - Mục đích: Decorator to cleanup the output and cache folders after each test.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-storage/graphrag_storage/tables/table.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `prepare_azurite_data(input_path, azure) -> Callable[[], None]`
    - Mục đích: Prepare the data for the Azurite tests.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestIndexer`
    - Methods chính: __run_indexer, __assert_indexer_outputs, __run_query, test_fixture
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit`

- Số file: **1**

#### File: `tests/unit/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/chunking`

- Số file: **3**

#### File: `tests/unit/chunking/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/chunking/test_chunker.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 191
- **Imports nổi bật**: typing (Any), unittest.mock (Mock, patch), graphrag.tokenizer.get_tokenizer (get_tokenizer), graphrag_chunking.bootstrap_nltk (bootstrap), graphrag_chunking.chunk_strategy_type (ChunkerType), graphrag_chunking.chunker_factory (create_chunker), graphrag_chunking.chunking_config (ChunkingConfig), graphrag_chunking.token_chunker (split_text_on_tokens), graphrag_llm.tokenizer (Tokenizer)
- **Hàm top-level**:
  - `test_split_text_str_empty()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_split_text_on_tokens()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_split_text_on_tokens_one_overlap()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_split_text_on_tokens_no_overlap()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MockTokenizer`
    - Methods chính: __init__, encode, decode
    - Được tham chiếu bởi (xấp xỉ): tests/unit/prompt_tune/test_load_docs_in_chunks.py
  - `TestRunSentences`
    - Methods chính: setup_method, test_basic_functionality, test_mixed_whitespace_handling
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestRunTokens`
    - Methods chính: test_basic_functionality
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/chunking/test_prepend_metadata.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 45
- **Imports nổi bật**: graphrag_chunking.transformers (add_metadata)
- **Hàm top-level**:
  - `test_add_metadata_one_row()`
    - Mục đích: Test prepending metadata to chunks
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_add_metadata_one_row_append()`
    - Mục đích: Test prepending metadata to chunks
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_add_metadata_multiple_rows()`
    - Mục đích: Test prepending metadata to chunks
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_add_metadata_custom_delimiters()`
    - Mục đích: Test prepending metadata to chunks
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/config`

- Số file: **13**

#### File: `tests/unit/config/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/prompt-a.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/prompt-b.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/prompt-c.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/prompt-d.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 61
- **Imports nổi bật**: os, pathlib (Path), unittest (mock), graphrag.config.load_config (load_config), graphrag.config.models.graph_rag_config (GraphRagConfig), tests.unit.config.utils (DEFAULT_COMPLETION_MODELS, DEFAULT_EMBEDDING_MODELS, FAKE_API_KEY, assert_graphrag_configs, get_default_graphrag_config)
- **Hàm top-level**:
  - `test_default_config() -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_load_minimal_config() -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_load_config_with_cli_overrides() -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_metrics_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 30
- **Mô tả module**: Test metrics configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (MetricsConfig, MetricsWriterType)
- **Hàm top-level**:
  - `test_file_metrics_writer_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_model_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 111
- **Mô tả module**: Test model configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (AuthMethod, LLMProviderType, ModelConfig), pydantic (ValidationError)
- **Hàm top-level**:
  - `test_litellm_provider_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_rate_limit_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 67
- **Mô tả module**: Test rate limit configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (RateLimitConfig, RateLimitType)
- **Hàm top-level**:
  - `test_sliding_window_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_retry_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 68
- **Mô tả module**: Test retry configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (RetryConfig, RetryType)
- **Hàm top-level**:
  - `test_exponential_backoff_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_immediate_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_template_engine_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 45
- **Mô tả module**: Test metrics configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (TemplateEngineConfig, TemplateEngineType, TemplateManagerType)
- **Hàm top-level**:
  - `test_template_engine_config_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/test_tokenizer_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 40
- **Mô tả module**: Test tokenizer configuration loading.
- **Imports nổi bật**: pytest, graphrag_llm.config (TokenizerConfig, TokenizerType)
- **Hàm top-level**:
  - `test_litellm_tokenizer_validation() -> None`
    - Mục đích: Test that missing required parameters raise validation errors.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/config/utils.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 380
- **Imports nổi bật**: dataclasses (asdict), graphrag.config.defaults, graphrag.config.models.basic_search_config (BasicSearchConfig), graphrag.config.models.cluster_graph_config (ClusterGraphConfig), graphrag.config.models.community_reports_config (CommunityReportsConfig), graphrag.config.models.drift_search_config (DRIFTSearchConfig), graphrag.config.models.embed_text_config (EmbedTextConfig), graphrag.config.models.extract_claims_config (ExtractClaimsConfig), graphrag.config.models.extract_graph_config (ExtractGraphConfig), graphrag.config.models.extract_graph_nlp_config (ExtractGraphNLPConfig, TextAnalyzerConfig), graphrag.config.models.global_search_config (GlobalSearchConfig), graphrag.config.models.graph_rag_config (GraphRagConfig)
- **Hàm top-level**:
  - `get_default_graphrag_config() -> GraphRagConfig`
    - Được tham chiếu bởi (xấp xỉ): tests/integration/logging/test_standard_logging.py, tests/unit/config/test_config.py, tests/verbs/test_create_base_text_units.py, tests/verbs/test_create_communities.py, tests/verbs/test_create_community_reports.py, tests/verbs/test_create_final_documents.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_retry_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_rate_limit_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_metrics_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_model_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_vector_store_configs(actual, expected)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_reporting_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_storage_config(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_cache_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_input_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_text_embedding_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_chunking_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_snapshots_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_extract_graph_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_text_analyzer_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_extract_graph_nlp_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_prune_graph_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_summarize_descriptions_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_community_reports_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_extract_claims_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_cluster_graph_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_local_search_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_global_search_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_drift_search_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_basic_search_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `assert_graphrag_configs(actual, expected) -> None`
    - Được tham chiếu bởi (xấp xỉ): tests/unit/config/test_config.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/config/fixtures/minimal_config`

- Số file: **1**

#### File: `tests/unit/config/fixtures/minimal_config/settings.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 12
- **Key cấu hình chính**: completion_models, default_completion_model, api_key, model_provider, model, embedding_models, default_embedding_model, api_key, model_provider, model
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/config/fixtures/minimal_config_missing_env_var`

- Số file: **1**

#### File: `tests/unit/config/fixtures/minimal_config_missing_env_var/settings.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 12
- **Key cấu hình chính**: completion_models, default_completion_model, api_key, model_provider, model, embedding_models, default_embedding_model, api_key, model_provider, model
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/config/fixtures/timestamp_dirs/20240812-120000`

- Số file: **1**

#### File: `tests/unit/config/fixtures/timestamp_dirs/20240812-120000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/graphrag_factory`

- Số file: **2**

#### File: `tests/unit/graphrag_factory/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphrag_factory/test_factory.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 67
- **Mô tả module**: Unit tests for graphrag_factory package.
- **Imports nổi bật**: abc (ABC, abstractmethod), graphrag_common.factory (Factory)
- **Hàm top-level**:
  - `test_factory() -> None`
    - Mục đích: Test the factory behavior.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestABC`
    - Mục đích: Test abstract base class.
    - Methods chính: get_value
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `ConcreteTestClass`
    - Mục đích: Concrete implementation of TestABC.
    - Methods chính: __init__, get_value
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/graphs`

- Số file: **6**

#### File: `tests/unit/graphs/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 5
- **Mô tả module**: Graph utility tests
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphs/nx_stable_lcc.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 67
- **Mô tả module**: NetworkX-based stable LCC utility, kept for side-by-side test comparisons.
- **Imports nổi bật**: html, typing (Any, cast), networkx
- **Hàm top-level**:
  - `_largest_connected_component(graph) -> nx.Graph`
    - Mục đích: Return the largest connected component of the graph (NX-based).
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `stable_largest_connected_component(graph) -> nx.Graph`
    - Mục đích: Return the largest connected component of the graph, with nodes and edges sorted in a stable way.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_stable_lcc.py, tests/unit/indexing/graph/utils/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_stabilize_graph(graph) -> nx.Graph`
    - Mục đích: Ensure an undirected graph with the same relationships will always be read the same way.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `normalize_node_names(graph) -> nx.Graph | nx.DiGraph`
    - Mục đích: Normalize node names.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphs/test_compute_degree.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 131
- **Mô tả module**: Side-by-side tests comparing NetworkX compute_degree with DataFrame-based compute_degree_df.
- **Imports nổi bật**: json, pathlib (Path), networkx, pandas, graphrag.graphs.compute_degree (compute_degree), pandas.testing (assert_frame_equal)
- **Hàm top-level**:
  - `_make_relationships(*edges) -> pd.DataFrame`
    - Mục đích: Build a relationships DataFrame from (source, target, weight) tuples.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py, tests/unit/graphs/test_stable_lcc.py, tests/unit/indexing/test_create_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_normalize(df) -> pd.DataFrame`
    - Mục đích: Sort by title and reset index for comparison.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_compute_degree_via_nx(relationships) -> pd.DataFrame`
    - Mục đích: Compute degree using NetworkX directly.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_simple_triangle()`
    - Mục đích: Three nodes forming a triangle — each should have degree 2.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_star_topology()`
    - Mục đích: One hub connected to many leaves.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py, tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_disconnected_components()`
    - Mục đích: Two separate components.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_single_edge()`
    - Mục đích: Simplest case: one edge, two nodes, each with degree 1.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_self_loop()`
    - Mục đích: A self-loop contributes degree 2 in NetworkX for undirected graphs.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_duplicate_edges()`
    - Mục đích: Duplicate edges in the DataFrame — NetworkX deduplicates, so should we check behavior.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py, tests/unit/graphs/test_modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_larger_graph()`
    - Mục đích: A larger graph to exercise multiple degree values.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_graph()`
    - Mục đích: Degree computation on the realistic A Christmas Carol fixture should match NetworkX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphs/test_connected_components.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 167
- **Mô tả module**: Side-by-side tests comparing NetworkX connected components with DataFrame-based implementation.
- **Imports nổi bật**: json, pathlib (Path), networkx, pandas, graphrag.graphs.connected_components (connected_components, largest_connected_component)
- **Hàm top-level**:
  - `_load_fixture() -> pd.DataFrame`
    - Mục đích: Load the realistic graph fixture as a relationships DataFrame.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_modularity.py, tests/unit/graphs/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_relationships(*edges) -> pd.DataFrame`
    - Mục đích: Build a relationships DataFrame from (source, target, weight) tuples.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/graphs/test_stable_lcc.py, tests/unit/indexing/test_create_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_nx_connected_components(relationships) -> list[set[str]]`
    - Mục đích: Compute connected components using NetworkX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_nx_largest_connected_component(relationships) -> set[str]`
    - Mục đích: Return the LCC using NetworkX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_single_component()`
    - Mục đích: Fully connected graph should have one component.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_two_components()`
    - Mục đích: Two disconnected pairs should give two components.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_three_components_lcc()`
    - Mục đích: LCC should pick the largest of three components.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_star_topology()`
    - Mục đích: Star should be a single component.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/indexing/test_finalize_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_duplicate_edges()`
    - Mục đích: Duplicate edges should not affect component membership.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/graphs/test_modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_empty_relationships()`
    - Mục đích: Empty edge list should produce no components.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_component_count()`
    - Mục đích: Component count should match NetworkX on the realistic fixture.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_component_sizes()`
    - Mục đích: Component sizes (sorted desc) should match NetworkX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_lcc_membership()`
    - Mục đích: LCC membership should be identical to NetworkX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_lcc_size()`
    - Mục đích: LCC should contain 535 nodes (known from the fixture).
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphs/test_modularity.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 263
- **Mô tả module**: Side-by-side tests for the DataFrame-based modularity utility.
- **Imports nổi bật**: json, math, collections (defaultdict), pathlib (Path), typing (Any), networkx, pandas, graphrag.graphs.modularity (modularity)
- **Hàm top-level**:
  - `_nx_modularity_component(intra_community_degree, total_community_degree, network_degree_sum, resolution) -> float`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_nx_modularity_components(graph, partitions, weight_attribute, resolution) -> dict[int, float]`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `nx_modularity(graph, partitions, weight_attribute, resolution) -> float`
    - Mục đích: NX reference: compute modularity from a networkx graph.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_load_fixture() -> pd.DataFrame`
    - Mục đích: Load the realistic graph fixture as a relationships DataFrame.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py, tests/unit/graphs/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_edges(*edges) -> pd.DataFrame`
    - Mục đích: Build a relationships DataFrame from (source, target, weight) tuples.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_cluster_graph.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_edges_to_nx(edges) -> nx.Graph`
    - Mục đích: Build an NX graph from an edges DataFrame.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_two_clear_communities()`
    - Mục đích: Two densely-connected communities with a weak bridge.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_single_community()`
    - Mục đích: All nodes in one community — modularity should be zero.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_every_node_own_community()`
    - Mục đích: Each node in its own community — modularity should be negative.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_reversed_edges()`
    - Mục đích: Reversed edge direction should not affect modularity (undirected).
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_weighted_edges()`
    - Mục đích: Different weights should affect modularity.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_custom_resolution()`
    - Mục đích: Resolution parameter should affect result and match NX.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_duplicate_edges()`
    - Mục đích: Duplicate edges (same pair, different weights) should match NX dedup.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/graphs/test_connected_components.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_reversed_duplicate_edges()`
    - Mục đích: Edge (A,B) and (B,A) should be treated as the same, keeping last weight.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_matches_nx()`
    - Mục đích: Modularity on the fixture graph should match NX for several partitions.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/graphs/test_stable_lcc.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 214
- **Mô tả module**: Side-by-side tests for the DataFrame-based stable LCC utility.
- **Imports nổi bật**: json, pathlib (Path), networkx, pandas, graphrag.graphs.stable_lcc (stable_lcc), pandas.testing (assert_frame_equal), tests.unit.graphs.nx_stable_lcc (stable_largest_connected_component)
- **Hàm top-level**:
  - `_load_fixture() -> pd.DataFrame`
    - Mục đích: Load the realistic graph fixture as a relationships DataFrame.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py, tests/unit/graphs/test_modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_relationships(*edges) -> pd.DataFrame`
    - Mục đích: Build a relationships DataFrame from (source, target, weight) tuples.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/graphs/test_connected_components.py, tests/unit/indexing/test_create_communities.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_nx_stable_lcc_node_set(relationships) -> set[str]`
    - Mục đích: Get the node set from the NX stable_largest_connected_component.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_nx_stable_lcc_edge_set(relationships) -> set[tuple[str, str]]`
    - Mục đích: Get the edge set from the NX stable_largest_connected_component.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_flipped_edges_produce_same_result()`
    - Mục đích: Same graph with edges in different direction should produce identical output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_shuffled_rows_produce_same_result()`
    - Mục đích: Different row order should produce identical output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_normalizes_node_names()`
    - Mục đích: Node names should be uppercased, stripped, and HTML-unescaped.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_filters_to_lcc()`
    - Mục đích: Only the largest component should remain.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_empty_relationships()`
    - Mục đích: Empty input should return empty output.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_connected_components.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_node_set_matches_nx()`
    - Mục đích: LCC node set should match the NX stable_largest_connected_component.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_edge_set_matches_nx()`
    - Mục đích: LCC edge set should match the NX stable_largest_connected_component.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_node_set_matches_nx()`
    - Mục đích: Fixture LCC nodes should match NX stable LCC.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_edge_set_matches_nx()`
    - Mục đích: Fixture LCC edges should match NX stable LCC.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_fixture_edges_are_sorted()`
    - Mục đích: Output edges should be sorted with source <= target and rows in order.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/graphs/fixtures`

- Số file: **1**

#### File: `tests/unit/graphs/fixtures/graph.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 7012
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/hasher`

- Số file: **2**

#### File: `tests/unit/hasher/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/hasher/test_hasher.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 105
- **Mô tả module**: Test hasher
- **Imports nổi bật**: graphrag_common.hasher (hash_data)
- **Hàm top-level**:
  - `test_hash_data() -> None`
    - Mục đích: Test hash data function.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing`

- Số file: **6**

#### File: `tests/unit/indexing/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/test_cluster_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 296
- **Mô tả module**: Tests for the cluster_graph operation.
- **Imports nổi bật**: pandas, pytest, graphrag.index.operations.cluster_graph (Communities, cluster_graph)
- **Hàm top-level**:
  - `_make_edges(rows) -> pd.DataFrame`
    - Mục đích: Build a minimal relationships DataFrame from (source, target, weight).
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_modularity.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_node_sets(clusters) -> list[set[str]]`
    - Mục đích: Extract sorted-by-level list of node sets from cluster output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestClusterGraphBasic`
    - Mục đích: Verify basic clustering on small synthetic graphs.
    - Methods chính: test_single_triangle, test_two_disconnected_cliques, test_lcc_filters_to_largest_component
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestEdgeNormalization`
    - Mục đích: Verify that direction normalization and deduplication work.
    - Methods chính: test_reversed_edges_produce_same_result, test_duplicate_edges_are_deduped, test_missing_weight_defaults_to_one
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestDeterminism`
    - Mục đích: Verify that seeding produces reproducible results.
    - Methods chính: test_same_seed_same_result, test_does_not_mutate_input
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestOutputStructure`
    - Mục đích: Verify the shape and types of the Communities output.
    - Methods chính: test_output_tuple_structure, test_level_zero_has_parent_minus_one, test_all_nodes_covered_at_each_level
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestClusterGraphRealData`
    - Mục đích: Regression tests using the shared test fixture data.
    - Methods chính: relationships, test_cluster_count, test_level_distribution, test_level_zero_nodes_sample
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/test_create_communities.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 621
- **Mô tả module**: Tests for the create_communities pure function.
- **Imports nổi bật**: uuid, typing (Any), numpy, pandas, pytest, graphrag.data_model.schemas (COMMUNITIES_FINAL_COLUMNS), graphrag.index.workflows.create_communities (_sanitize_row, create_communities), graphrag_storage.tables.csv_table (CSVTable), graphrag_storage.tables.table (Table)
- **Hàm top-level**:
  - `_run_create_communities(title_to_entity_id, relationships, **kwargs) -> pd.DataFrame`
    - Mục đích: Helper that runs create_communities with fake tables and returns all rows as a DataFrame.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_title_to_entity_id(rows) -> dict[str, str]`
    - Mục đích: Build a title-to-entity-id mapping from (id, title) pairs.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_relationships(rows) -> pd.DataFrame`
    - Mục đích: Build a minimal relationships DataFrame.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/graphs/test_compute_degree.py, tests/unit/graphs/test_connected_components.py, tests/unit/graphs/test_stable_lcc.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `two_triangles()`
    - Mục đích: Two disconnected triangles: {A,B,C} and {D,E,F}.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `FakeTable`
    - Mục đích: In-memory table that collects written rows for test assertions.
    - Methods chính: __init__, write
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_finalize_graph.py
  - `FakeEntitiesTable`
    - Mục đích: In-memory read-only table that supports async iteration.
    - Methods chính: __init__, __aiter__, __anext__, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestOutputSchema`
    - Mục đích: Verify the output DataFrame has the expected column schema.
    - Methods chính: test_has_all_final_columns, test_column_order_matches_schema
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestMetadataFields`
    - Mục đích: Verify computed metadata fields like id, title, size, period.
    - Methods chính: test_uuid_ids, test_title_format, test_human_readable_id_equals_community, test_size_equals_entity_count, test_period_is_iso_date
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestEntityAggregation`
    - Mục đích: Verify that entity_ids are correctly aggregated per community.
    - Methods chính: test_entity_ids_per_community, test_entity_ids_are_lists
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestRelationshipAggregation`
    - Mục đích: Verify that relationship_ids and text_unit_ids are correctly
    - Methods chính: test_relationship_ids_per_community, test_text_unit_ids_per_community, test_lists_are_sorted_and_deduplicated, test_cross_community_relationships_excluded
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestParentChildTree`
    - Mục đích: Verify the parent-child tree structure is consistent.
    - Methods chính: test_level_zero_parent_is_minus_one, test_leaf_communities_have_empty_children, test_parent_child_bidirectional_consistency_real_data
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestLccFiltering`
    - Mục đích: Verify LCC filtering interaction with create_communities.
    - Methods chính: test_lcc_reduces_community_count
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestRealDataRegression`
    - Mục đích: Regression tests using the shared test fixture data.
    - Methods chính: real_result, test_row_count, test_level_distribution, test_values_match_golden_file, test_communities_with_children
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestSanitizeRow`
    - Mục đích: Verify numpy types are converted to native Python types.
    - Methods chính: test_ndarray_to_list, test_empty_ndarray_to_empty_list, test_np_integer_to_int, test_np_floating_to_float, test_native_types_pass_through, test_mixed_row
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/test_finalize_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 445
- **Mô tả module**: Tests for the finalize_graph streaming functions.
- **Imports nổi bật**: typing (Any), pytest, graphrag.data_model.schemas (ENTITIES_FINAL_COLUMNS, RELATIONSHIPS_FINAL_COLUMNS), graphrag.index.operations.finalize_entities (finalize_entities), graphrag.index.operations.finalize_relationships (finalize_relationships), graphrag.index.workflows.finalize_graph (_build_degree_map, finalize_graph), graphrag_storage.tables.table (Table)
- **Hàm top-level**:
  - `_make_entity_row(title, entity_type, description, frequency) -> dict[str, Any]`
    - Mục đích: Build a minimal entity row matching pre-finalization shape.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_relationship_row(source, target, weight, description) -> dict[str, Any]`
    - Mục đích: Build a minimal relationship row matching pre-finalization shape.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `FakeTable`
    - Mục đích: In-memory table that supports async iteration and write collection.
    - Methods chính: __init__, __aiter__, __anext__, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): tests/unit/indexing/test_create_communities.py
  - `TestBuildDegreeMap`
    - Mục đích: Tests for the streaming _build_degree_map helper.
    - Methods chính: test_simple_triangle, test_star_topology, test_duplicate_edges_deduplicated, test_reversed_duplicate_edges_deduplicated, test_empty_table, test_single_edge, test_disconnected_components
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFinalizeEntities`
    - Mục đích: Tests for stream-finalize entity rows.
    - Methods chính: test_enriches_with_degree, test_missing_degree_defaults_to_zero, test_deduplicates_by_title, test_skips_empty_title, test_assigns_sequential_human_readable_ids, test_assigns_unique_ids, test_output_columns_match_schema, test_returns_sample_rows_up_to_five, test_empty_table
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFinalizeRelationships`
    - Mục đích: Tests for stream-finalize relationship rows.
    - Methods chính: test_enriches_with_combined_degree, test_missing_degree_defaults_to_zero, test_deduplicates_by_source_target, test_reversed_pair_not_deduplicated, test_assigns_sequential_human_readable_ids, test_assigns_unique_ids, test_output_columns_match_schema, test_returns_sample_rows_up_to_five, test_empty_table
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFinalizeGraph`
    - Mục đích: Tests for the orchestrating finalize_graph function.
    - Methods chính: test_produces_entities_and_relationships_keys, test_degree_flows_through_to_entities, test_combined_degree_flows_through_to_relationships, test_empty_graph, test_all_rows_written
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/test_init_content.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 30
- **Imports nổi bật**: re, typing (Any, cast), yaml, graphrag.config.init_content (INIT_YAML), graphrag.config.models.graph_rag_config (GraphRagConfig)
- **Hàm top-level**:
  - `test_init_yaml()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_init_yaml_uncommented()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/test_profiling.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 96
- **Mô tả module**: Unit tests for WorkflowProfiler.
- **Imports nổi bật**: time, graphrag.index.run.profiling (WorkflowProfiler), graphrag.index.typing.stats (WorkflowMetrics)
- **Class top-level**:
  - `TestWorkflowProfiler`
    - Mục đích: Tests for the WorkflowProfiler context manager.
    - Methods chính: test_captures_time, test_captures_peak_memory, test_captures_memory_delta, test_captures_tracemalloc_overhead, test_returns_workflow_metrics_dataclass, test_all_metrics_populated, test_handles_exception_in_context, test_multiple_profilers_independent
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/cache`

- Số file: **2**

#### File: `tests/unit/indexing/cache/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/cache/test_file_pipeline_cache.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 81
- **Imports nổi bật**: asyncio, os, unittest, graphrag_cache (CacheConfig, CacheType), graphrag_cache (create_cache), graphrag_storage (StorageConfig, StorageType)
- **Hàm top-level**:
  - `create_cache()`
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-cache/README.md, packages/graphrag-cache/example_notebooks/basic_cache_example.ipynb, packages/graphrag-cache/example_notebooks/custom_cache_example.ipynb, packages/graphrag-cache/graphrag_cache/__init__.py, packages/graphrag-cache/graphrag_cache/cache_factory.py, packages/graphrag-llm/notebooks/05_caching.ipynb
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestFilePipelineCache`
    - Methods chính: setUp, tearDown, test_cache_clear, test_child_cache, test_cache_has, test_get_set
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/graph`

- Số file: **1**

#### File: `tests/unit/indexing/graph/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/graph/extractors`

- Số file: **1**

#### File: `tests/unit/indexing/graph/extractors/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/graph/extractors/community_reports`

- Số file: **2**

#### File: `tests/unit/indexing/graph/extractors/community_reports/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 222
- **Imports nổi bật**: math, platform, graphrag.index.operations.summarize_communities.graph_context.sort_context (sort_context), graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `test_sort_context()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_sort_context_max_tokens()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/graph/utils`

- Số file: **2**

#### File: `tests/unit/indexing/graph/utils/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/graph/utils/test_stable_lcc.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 46
- **Imports nổi bật**: unittest, networkx, tests.unit.graphs.nx_stable_lcc (stable_largest_connected_component)
- **Class top-level**:
  - `TestStableLCC`
    - Methods chính: test_undirected_graph_run_twice_produces_same_graph, _create_strongly_connected_graph, _create_strongly_connected_graph_with_edges_flipped
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input`

- Số file: **7**

#### File: `tests/unit/indexing/input/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_csv_loader.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 80
- **Imports nổi bật**: graphrag_input (InputConfig, InputType, create_input_reader), graphrag_storage (StorageConfig, create_storage)
- **Hàm top-level**:
  - `test_csv_loader_one_file()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_csv_loader_one_file_with_title()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_csv_loader_multiple_files()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_csv_loader_preserves_multiline_fields(tmp_path)`
    - Mục đích: Multiline quoted CSV fields must retain their internal newlines.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_json_loader.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 72
- **Imports nổi bật**: graphrag_input (InputConfig, InputType, create_input_reader), graphrag_storage (StorageConfig, create_storage)
- **Hàm top-level**:
  - `test_json_loader_one_file_one_object()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_json_loader_one_file_multiple_objects()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_json_loader_one_file_with_title()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_json_loader_multiple_files()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_jsonl_loader.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 43
- **Imports nổi bật**: graphrag_input (InputConfig, InputType, create_input_reader), graphrag_storage (StorageConfig, create_storage)
- **Hàm top-level**:
  - `test_jsonl_loader_one_file_multiple_objects()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_jsonl_loader_one_file_with_title()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_markitdown_loader.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 27
- **Imports nổi bật**: graphrag_input (InputConfig, InputType, create_input_reader), graphrag_storage (StorageConfig, create_storage)
- **Hàm top-level**:
  - `test_markitdown_loader_one_file()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_text_document.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 77
- **Imports nổi bật**: pytest, graphrag_input (get_property)
- **Hàm top-level**:
  - `test_get_property_single_level()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_two_levels()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_three_levels()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_returns_dict()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_missing_key_raises()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_missing_nested_key_raises()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_non_dict_intermediate_raises()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_empty_dict_raises()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_with_none_value()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_with_list_value()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_list_intermediate_raises()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_numeric_value()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_property_boolean_value()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/test_text_loader.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 37
- **Imports nổi bật**: graphrag_input (InputConfig, InputType, create_input_reader), graphrag_storage (StorageConfig, create_storage)
- **Hàm top-level**:
  - `test_text_loader_one_file()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_text_loader_multiple_files()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/multiple-csvs`

- Số file: **3**

#### File: `tests/unit/indexing/input/data/multiple-csvs/input1.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/data/multiple-csvs/input2.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/data/multiple-csvs/input3.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/multiple-jsons`

- Số file: **2**

#### File: `tests/unit/indexing/input/data/multiple-jsons/input1.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 11
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/data/multiple-jsons/input2.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 4
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/multiple-txts`

- Số file: **2**

#### File: `tests/unit/indexing/input/data/multiple-txts/input1.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/input/data/multiple-txts/input2.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-csv`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-csv/input.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-html`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-html/input.html`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-json-multiple-objects`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-json-multiple-objects/input.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 11
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-json-one-object`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-json-one-object/input.json`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 4
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-jsonl`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-jsonl/input.jsonl`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/input/data/one-txt`

- Số file: **1**

#### File: `tests/unit/indexing/input/data/one-txt/input.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/operations`

- Số file: **2**

#### File: `tests/unit/indexing/operations/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/operations/test_extract_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 302
- **Mô tả module**: Tests for extract_graph merge and orphan-filtering operations.
- **Imports nổi bật**: pandas, graphrag.index.operations.extract_graph.extract_graph (_merge_entities, _merge_relationships), graphrag.index.operations.extract_graph.utils (filter_orphan_relationships)
- **Hàm top-level**:
  - `_entity_row(title, entity_type, description, source_id) -> dict`
    - Mục đích: Build a single raw entity row as produced by the graph extractor.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_relationship_row(source, target, weight, description, source_id) -> dict`
    - Mục đích: Build a single raw relationship row as produced by the graph extractor.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestMergeEntities`
    - Mục đích: Tests for the _merge_entities aggregation helper.
    - Methods chính: test_groups_by_title_and_type, test_different_types_stay_separate, test_empty_input
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestMergeRelationships`
    - Mục đích: Tests for the _merge_relationships aggregation helper.
    - Methods chính: test_groups_by_source_target, test_distinct_pairs_stay_separate, test_empty_input
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFilterOrphanRelationships`
    - Mục đích: Tests for orphan relationship filtering.
    - Methods chính: test_all_valid_relationships_kept, test_removes_relationship_with_missing_source, test_removes_relationship_with_missing_target, test_removes_relationship_with_both_missing, test_keeps_valid_drops_orphan_mixed, test_empty_entities_drops_all_relationships, test_empty_relationships_returns_empty, test_preserves_all_columns, test_multi_text_unit_orphan, test_resets_index_after_filter
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/operations/embed_text`

- Số file: **2**

#### File: `tests/unit/indexing/operations/embed_text/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/operations/embed_text/test_embed_text.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 419
- **Mô tả module**: Unit tests for the streaming embed_text operation.
- **Imports nổi bật**: collections.abc (AsyncIterator), typing (Any), unittest.mock (AsyncMock, MagicMock, patch), numpy, pytest, graphrag.callbacks.noop_workflow_callbacks (NoopWorkflowCallbacks), graphrag.index.operations.embed_text.embed_text (embed_text), graphrag.index.operations.embed_text.run_embed_text (TextEmbeddingResult), graphrag_storage.tables.table (Table)
- **Hàm top-level**:
  - `_make_mock_vector_store()`
    - Mục đích: Create a mock vector store with create_index and load_documents.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_mock_model(embedding_values)`
    - Mục đích: Create a mock model that returns fixed embeddings.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_make_embedding_result(count, values) -> TextEmbeddingResult`
    - Mục đích: Build a TextEmbeddingResult with count copies of values.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_basic()`
    - Mục đích: Verify basic embedding: rows flow through to vector store and output table.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_batching()`
    - Mục đích: Verify rows are flushed in batches sized by batch_size * num_threads.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_pretransformed_rows()`
    - Mục đích: Verify rows pre-transformed by table layer are embedded correctly.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_none_values_filled()`
    - Mục đích: Verify None embed_column values are replaced with empty string.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_no_output_table()`
    - Mục đích: Verify embedding works without an output table (no snapshot).
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_empty_input()`
    - Mục đích: Verify zero rows returns zero count with no calls.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_numpy_array_vectors()`
    - Mục đích: Verify np.ndarray embeddings are converted to plain lists.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_embed_text_partial_none_embeddings()`
    - Mục đích: Verify rows with None embeddings are skipped in store and output.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `FakeInputTable`
    - Mục đích: In-memory table that yields rows via async iteration.
    - Methods chính: __init__, __aiter__, _iter, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `FakeOutputTable`
    - Mục đích: Collects rows written via write() for assertion.
    - Methods chính: __init__, __aiter__, _iter, length, has, write, close
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/update`

- Số file: **2**

#### File: `tests/unit/indexing/update/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/update/test_update_relationships.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 228
- **Mô tả module**: Tests for incremental update merge operations.
- **Imports nổi bật**: pandas, graphrag.index.operations.extract_graph.utils (filter_orphan_relationships), graphrag.index.update.relationships (_update_and_merge_relationships)
- **Hàm top-level**:
  - `_finalized_entity_row(title, entity_id, human_readable_id, entity_type, description, frequency, degree) -> dict`
    - Mục đích: Build a finalized entity row matching ENTITIES_FINAL_COLUMNS shape.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_finalized_relationship_row(source, target, relationship_id, human_readable_id, weight, description, combined_degree) -> dict`
    - Mục đích: Build a finalized relationship row matching RELATIONSHIPS_FINAL_COLUMNS.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestUpdateAndMergeRelationships`
    - Mục đích: Tests for _update_and_merge_relationships.
    - Methods chính: test_merges_old_and_delta, test_overlapping_pairs_aggregate, test_human_readable_ids_incremented
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestUpdatePathOrphanFiltering`
    - Mục đích: Tests that orphan relationships are caught in the update path.
    - Methods chính: test_delta_introduces_orphan_source, test_delta_introduces_orphan_target, test_delta_introduces_orphan_both_endpoints, test_all_valid_after_update, test_old_relationship_becomes_orphan_after_entity_merge
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/verbs`

- Số file: **1**

#### File: `tests/unit/indexing/verbs/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/verbs/entities`

- Số file: **1**

#### File: `tests/unit/indexing/verbs/entities/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/verbs/entities/extraction`

- Số file: **1**

#### File: `tests/unit/indexing/verbs/entities/extraction/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/verbs/entities/extraction/strategies`

- Số file: **1**

#### File: `tests/unit/indexing/verbs/entities/extraction/strategies/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence`

- Số file: **2**

#### File: `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 80
- **Imports nổi bật**: unittest, graphrag.index.operations.extract_graph.extract_graph (_run_extract_graph), graphrag.prompts.index.extract_graph (GRAPH_EXTRACTION_PROMPT), graphrag_llm.completion (create_completion), graphrag_llm.config (LLMProviderType, ModelConfig)
- **Class top-level**:
  - `TestRunChain`
    - Methods chính: test_run_extract_graph_single_document_correct_entities_returned, test_run_extract_graph_single_document_correct_edges_returned, test_run_extract_graph_single_document_source_ids_mapped
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/load_config`

- Số file: **3**

#### File: `tests/unit/load_config/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 28
- **Mô tả module**: Config models for load_config unit tests.
- **Imports nổi bật**: pydantic (BaseModel, ConfigDict, Field)
- **Class top-level**:
  - `TestNestedModel`
    - Mục đích: Test nested model.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestConfigModel`
    - Mục đích: Test configuration model.
    - Được tham chiếu bởi (xấp xỉ): tests/unit/load_config/test_load_config.py
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/test_load_config.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 158
- **Mô tả module**: Unit tests for graphrag-config.load_config.
- **Imports nổi bật**: os, pathlib (Path), pytest, graphrag_common.config (ConfigParsingError, load_config), pydantic (ValidationError), config (TestConfigModel)
- **Hàm top-level**:
  - `test_load_config_validation()`
    - Mục đích: Test loading config validation.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_load_config()`
    - Mục đích: Test loading configuration.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/load_config/fixtures`

- Số file: **6**

#### File: `tests/unit/load_config/fixtures/config.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 10
- **Key cấu hình chính**: name, value, nested, nested_str, nested_int, nested_list, nested_int, nested_int
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/fixtures/config_with_env.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 10
- **Key cấu hình chính**: name, value, nested, nested_str, nested_int, nested_list, nested_int, nested_int
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/fixtures/invalid_config.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 1
- **Key cấu hình chính**: name
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/fixtures/invalid_config_format.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 8
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/fixtures/settings.yaml`
- **Loại**: config/data
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 10
- **Key cấu hình chính**: name, value, nested, nested_str, nested_int, nested_list, nested_int, nested_int
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/load_config/fixtures/test.env`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/prompt_tune`

- Số file: **2**

#### File: `tests/unit/prompt_tune/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 5
- **Mô tả module**: Unit tests for prompt_tune module.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/prompt_tune/test_load_docs_in_chunks.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 293
- **Mô tả module**: Unit tests for load_docs_in_chunks function.
- **Imports nổi bật**: logging, dataclasses (dataclass), typing (Any), unittest.mock (AsyncMock, MagicMock, patch), pytest, graphrag.prompt_tune.loader.input (load_docs_in_chunks), graphrag.prompt_tune.types (DocSelectionType)
- **Hàm top-level**:
  - `mock_config()`
    - Mục đích: Create a mock GraphRagConfig.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `mock_logger()`
    - Mục đích: Create a mock logger.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `sample_documents()`
    - Mục đích: Create sample documents for testing.
    - Được tham chiếu bởi (xấp xỉ): packages/graphrag-vectors/example_notebooks/custom_vector_store.ipynb, tests/integration/vector_stores/test_azure_ai_search.py, tests/integration/vector_stores/test_lancedb.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MockTextDocument`
    - Mục đích: Mock TextDocument for testing.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `MockTokenizer`
    - Mục đích: Mock tokenizer for testing.
    - Methods chính: encode, decode
    - Được tham chiếu bởi (xấp xỉ): tests/unit/chunking/test_chunker.py
  - `MockChunk`
    - Mục đích: Mock chunk result.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `MockChunker`
    - Mục đích: Mock chunker for testing.
    - Methods chính: chunk
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `MockEmbeddingModel`
    - Mục đích: Mock embedding model for testing.
    - Methods chính: __init__
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestLoadDocsInChunks`
    - Mục đích: Tests for load_docs_in_chunks function.
    - Methods chính: test_top_selection_returns_limited_chunks, test_random_selection_returns_correct_count, test_escapes_braces_in_output, test_limit_out_of_range_uses_default, test_chunks_all_documents
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query`

- Số file: **1**

#### File: `tests/unit/query/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/context_builder`

- Số file: **3**

#### File: `tests/unit/query/context_builder/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/query/context_builder/dynamic_community_selection.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 206
- **Mô tả module**: Tests for dynamic community selection with type handling.
- **Imports nổi bật**: unittest.mock (MagicMock), graphrag.data_model.community (Community), graphrag.data_model.community_report (CommunityReport), graphrag.query.context_builder.dynamic_community_selection (DynamicCommunitySelection)
- **Hàm top-level**:
  - `create_mock_tokenizer() -> MagicMock`
    - Mục đích: Create a mock tokenizer.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `create_mock_model() -> MagicMock`
    - Mục đích: Create a mock chat model.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_dynamic_community_selection_handles_int_children()`
    - Mục đích: Test that DynamicCommunitySelection correctly handles children IDs as integers.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_dynamic_community_selection_handles_str_children()`
    - Mục đích: Test that DynamicCommunitySelection works correctly with string children IDs.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/query/context_builder/test_entity_extraction.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 167
- **Imports nổi bật**: typing (Any), graphrag.data_model.entity (Entity), graphrag.query.context_builder.entity_extraction (EntityVectorStoreKey, map_query_to_entities), graphrag_llm.config (LLMProviderType, ModelConfig), graphrag_llm.embedding (create_embedding), graphrag_vectors (TextEmbedder, VectorStore, VectorStoreDocument, VectorStoreSearchResult)
- **Hàm top-level**:
  - `test_map_query_to_entities()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `MockVectorStore`
    - Methods chính: __init__, connect, create_index, load_documents, insert, similarity_search_by_vector, similarity_search_by_text, search_by_id, count, remove, update
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/defaults/output/20240812-120000`

- Số file: **1**

#### File: `tests/unit/query/data/defaults/output/20240812-120000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/defaults/output/20240812-121000`

- Số file: **1**

#### File: `tests/unit/query/data/defaults/output/20240812-121000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/empty/something-else`

- Số file: **1**

#### File: `tests/unit/query/data/empty/something-else/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/hidden/output`

- Số file: **1**

#### File: `tests/unit/query/data/hidden/output/.hidden`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/hidden/output/.another`

- Số file: **1**

#### File: `tests/unit/query/data/hidden/output/.another/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/hidden/output/20240812-120000`

- Số file: **1**

#### File: `tests/unit/query/data/hidden/output/20240812-120000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/hidden/output/20240812-121000`

- Số file: **1**

#### File: `tests/unit/query/data/hidden/output/20240812-121000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/non-numeric/output/20240812-120000`

- Số file: **1**

#### File: `tests/unit/query/data/non-numeric/output/20240812-120000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/non-numeric/output/20240812-121000`

- Số file: **1**

#### File: `tests/unit/query/data/non-numeric/output/20240812-121000/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/data/non-numeric/output/something-else`

- Số file: **1**

#### File: `tests/unit/query/data/non-numeric/output/something-else/empty.txt`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/input`

- Số file: **1**

#### File: `tests/unit/query/input/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/query/input/retrieval`

- Số file: **2**

#### File: `tests/unit/query/input/retrieval/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/query/input/retrieval/test_entities.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 168
- **Imports nổi bật**: graphrag.data_model.entity (Entity), graphrag.query.input.retrieval.entities (get_entity_by_id, get_entity_by_key)
- **Hàm top-level**:
  - `test_get_entity_by_id()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_get_entity_by_key()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/storage`

- Số file: **4**

#### File: `tests/unit/storage/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/storage/test_csv_table.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 239
- **Mô tả module**: Tests for CSVTable temp-file write strategy and streaming behavior.
- **Imports nổi bật**: csv, pathlib (Path), typing (Any), pytest, graphrag_storage.file_storage (FileStorage), graphrag_storage.tables.csv_table (CSVTable)
- **Hàm top-level**:
  - `_read_csv_rows(path) -> list[dict[str, Any]]`
    - Mục đích: Read all rows from a CSV file as dicts.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_write_seed_csv(path, rows) -> None`
    - Mục đích: Write seed rows to a CSV file for test setup.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `TestCSVTableTruncateWrite`
    - Mục đích: Verify the temp-file write strategy when truncate=True.
    - Methods chính: storage, seed_file, test_original_readable_during_writes, test_temp_file_replaces_original_on_close, test_no_temp_file_left_after_close, test_multiple_writes_accumulate_in_temp, test_concurrent_read_and_write_same_file
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestCSVTableAppendWrite`
    - Mục đích: Verify append behavior when truncate=False.
    - Methods chính: storage, test_append_to_existing_file, test_append_creates_file_with_header, test_no_temp_file_used_for_append
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestCSVTableCloseIdempotent`
    - Mục đích: Verify close() can be called multiple times safely.
    - Methods chính: storage, test_double_close_is_safe, test_close_without_writes_is_safe
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/storage/test_csv_table_provider.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 120
- **Imports nổi bật**: unittest, io (StringIO), pandas, pytest, graphrag_storage (StorageConfig, StorageType, create_storage), graphrag_storage.tables.csv_table_provider (CSVTableProvider)
- **Class top-level**:
  - `TestCSVTableProvider`
    - Mục đích: Test suite for CSVTableProvider.
    - Methods chính: setUp, asyncTearDown, test_write_and_read, test_read_nonexistent_table_raises_error, test_empty_dataframe, test_dataframe_with_multiple_types, test_storage_persistence, test_has, test_list
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/storage/test_parquet_table_provider.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 91
- **Imports nổi bật**: unittest, io (BytesIO), pandas, pytest, graphrag_storage (StorageConfig, StorageType, create_storage), graphrag_storage.tables.parquet_table_provider (ParquetTableProvider)
- **Class top-level**:
  - `TestParquetTableProvider`
    - Methods chính: setUp, asyncTearDown, test_write_and_read, test_read_nonexistent_table_raises_error, test_empty_dataframe, test_dataframe_with_multiple_types, test_storage_persistence, test_has
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/utils`

- Số file: **2**

#### File: `tests/unit/utils/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/utils/test_encoding.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 21
- **Imports nổi bật**: graphrag.tokenizer.get_tokenizer (get_tokenizer)
- **Hàm top-level**:
  - `test_encode_basic()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_num_tokens_empty_input()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/unit/vector_stores`

- Số file: **3**

#### File: `tests/unit/vector_stores/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/vector_stores/test_filtering.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 324
- **Mô tả module**: Unit tests for the filtering module (no backend required).
- **Imports nổi bật**: json, graphrag_vectors.filtering (AndExpr, Condition, F, FilterExpr, NotExpr, Operator, OrExpr)
- **Class top-level**:
  - `TestConditionEvaluate`
    - Mục đích: Tests for Condition.evaluate() client-side evaluation.
    - Methods chính: test_eq, test_ne, test_gt, test_gte, test_lt, test_lte, test_in, test_missing_field_returns_false
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestAndEvaluate`
    - Mục đích: Tests for AndExpr.evaluate() client-side evaluation.
    - Methods chính: test_all_true, test_one_false
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestOrEvaluate`
    - Mục đích: Tests for OrExpr.evaluate() client-side evaluation.
    - Methods chính: test_one_true, test_none_true
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestNotEvaluate`
    - Mục đích: Tests for NotExpr.evaluate() client-side evaluation.
    - Methods chính: test_negates_true, test_negates_false
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFBuilder`
    - Mục đích: Tests for the F fluent builder.
    - Methods chính: test_eq_produces_condition, test_ne, test_gt, test_gte, test_lt, test_lte, test_in
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestOperatorOverloads`
    - Mục đích: Tests for & | ~ operator overloads on expression types.
    - Methods chính: test_and_two_conditions, test_or_two_conditions, test_not_condition, test_not_and, test_and_or_nesting
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestFlattening`
    - Mục đích: Tests for AND/OR expression flattening (associativity).
    - Methods chính: test_and_flattening, test_or_flattening
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestDoubleNegation`
    - Mục đích: Tests for double negation behavior.
    - Methods chính: test_double_negation
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestJsonRoundtrip`
    - Mục đích: Tests for JSON serialization/deserialization round-trips.
    - Methods chính: _roundtrip, test_condition_roundtrip, test_and_roundtrip, test_or_roundtrip, test_not_roundtrip, test_complex_nested_roundtrip
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/unit/vector_stores/test_timestamp.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 113
- **Mô tả module**: Unit tests for the timestamp module (no backend required).
- **Imports nổi bật**: pytest, graphrag_vectors.timestamp (TIMESTAMP_FIELDS, _timestamp_fields_for, explode_timestamp)
- **Class top-level**:
  - `TestExplodeTimestamp`
    - Mục đích: Tests for explode_timestamp().
    - Methods chính: test_basic_explosion, test_all_keys_present, test_empty_string_returns_empty, test_none_returns_empty
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestExplodeTimestampQuarterBoundaries`
    - Mục đích: Tests for correct quarter assignment across all months.
    - Methods chính: test_quarter
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestTimestampFieldsForPrefix`
    - Mục đích: Tests for _timestamp_fields_for() helper.
    - Methods chính: test_produces_correct_keys, test_types
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
  - `TestTimestampFieldsConstant`
    - Mục đích: Tests for the TIMESTAMP_FIELDS combined constant.
    - Methods chính: test_contains_create_and_update_fields, test_total_count
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/verbs`

- Số file: **15**

#### File: `tests/verbs/__init__.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 3
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_create_base_text_units.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 36
- **Imports nổi bật**: graphrag.index.workflows.create_base_text_units (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (compare_outputs, create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_create_base_text_units()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_create_communities.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 48
- **Imports nổi bật**: graphrag.data_model.schemas (COMMUNITIES_FINAL_COLUMNS), graphrag.index.workflows.create_communities (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (compare_outputs, create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_create_communities()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_create_community_reports.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 71
- **Imports nổi bật**: graphrag.data_model.schemas (COMMUNITY_REPORTS_FINAL_COLUMNS), graphrag.index.operations.summarize_communities.community_reports_extractor (CommunityReportResponse, FindingModel), graphrag.index.workflows.create_community_reports (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (compare_outputs, create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_create_community_reports()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_create_final_documents.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 35
- **Imports nổi bật**: graphrag.data_model.schemas (DOCUMENTS_FINAL_COLUMNS), graphrag.index.workflows.create_final_documents (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (compare_outputs, create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_create_final_documents()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_create_final_text_units.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 142
- **Imports nổi bật**: typing (Any), pandas, graphrag.data_model.row_transformers (transform_entity_row, transform_relationship_row, transform_text_unit_row), graphrag.data_model.schemas (TEXT_UNITS_FINAL_COLUMNS), graphrag.index.workflows.create_final_text_units (create_final_text_units, run_workflow), graphrag_storage.file_storage (FileStorage), graphrag_storage.tables.csv_table (CSVTable), graphrag_storage.tables.table (Table), tests.unit.config.utils (get_default_graphrag_config), util (compare_outputs, create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_create_final_text_units()`
    - Mục đích: End-to-end test using ParquetTableProvider via run_workflow.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_create_final_text_units_csv_path()`
    - Mục đích: Exercise create_final_text_units through real CSVTable reads.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Class top-level**:
  - `_FakeWriteTable`
    - Mục đích: In-memory write-only table that collects rows.
    - Methods chính: __init__, write, __aiter__, length, has, close
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_extract_covariates.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 74
- **Imports nổi bật**: graphrag.data_model.schemas (COVARIATES_FINAL_COLUMNS), graphrag.index.workflows.extract_covariates (run_workflow), graphrag_llm.config (LLMProviderType), pandas.testing (assert_series_equal), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_extract_covariates()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_extract_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 65
- **Imports nổi bật**: graphrag.index.workflows.extract_graph (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context)
- **Hàm top-level**:
  - `test_extract_graph()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_extract_graph_nlp.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 31
- **Imports nổi bật**: graphrag.index.workflows.extract_graph_nlp (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context)
- **Hàm top-level**:
  - `test_extract_graph_nlp()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_finalize_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 47
- **Imports nổi bật**: graphrag.data_model.schemas (ENTITIES_FINAL_COLUMNS, RELATIONSHIPS_FINAL_COLUMNS), graphrag.index.workflows.finalize_graph (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context, load_test_table)
- **Hàm top-level**:
  - `test_finalize_graph()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `_prep_tables()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_generate_text_embeddings.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 54
- **Imports nổi bật**: graphrag.config.embeddings (all_embeddings), graphrag.index.workflows.generate_text_embeddings (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context)
- **Hàm top-level**:
  - `test_generate_text_embeddings()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_pipeline_state.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 55
- **Mô tả module**: Tests for pipeline state passthrough.
- **Imports nổi bật**: graphrag.config.models.graph_rag_config (GraphRagConfig), graphrag.index.run.utils (create_run_context), graphrag.index.typing.context (PipelineRunContext), graphrag.index.typing.workflow (WorkflowFunctionOutput), graphrag.index.workflows.factory (PipelineFactory), tests.unit.config.utils (get_default_graphrag_config)
- **Hàm top-level**:
  - `run_workflow_1(_config, context)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `run_workflow_2(_config, context)`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_pipeline_state()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `test_pipeline_existing_state()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_prune_graph.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 29
- **Imports nổi bật**: graphrag.config.models.prune_graph_config (PruneGraphConfig), graphrag.index.workflows.prune_graph (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context)
- **Hàm top-level**:
  - `test_prune_graph()`
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/test_update_text_embeddings.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 66
- **Mô tả module**: Verb test for the update_text_embeddings workflow.
- **Imports nổi bật**: unittest.mock (patch), graphrag.config.embeddings (all_embeddings), graphrag.index.workflows.update_text_embeddings (run_workflow), tests.unit.config.utils (get_default_graphrag_config), util (create_test_context)
- **Hàm top-level**:
  - `test_update_text_embeddings()`
    - Mục đích: Verify update_text_embeddings produces embedding tables.
    - Được tham chiếu bởi (xấp xỉ): chưa thấy tham chiếu rõ ràng ngoài nội bộ file.
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/util.py`
- **Loại**: python
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Số dòng**: 67
- **Imports nổi bật**: pandas, graphrag.index.run.utils (create_run_context), graphrag.index.typing.context (PipelineRunContext), pandas.testing (assert_series_equal)
- **Hàm top-level**:
  - `create_test_context(storage) -> PipelineRunContext`
    - Mục đích: Create a test context with tables loaded into storage storage.
    - Được tham chiếu bởi (xấp xỉ): tests/verbs/test_create_base_text_units.py, tests/verbs/test_create_communities.py, tests/verbs/test_create_community_reports.py, tests/verbs/test_create_final_documents.py, tests/verbs/test_create_final_text_units.py, tests/verbs/test_extract_covariates.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `load_test_table(output) -> pd.DataFrame`
    - Mục đích: Pass in the workflow output (generally the workflow name)
    - Được tham chiếu bởi (xấp xỉ): tests/verbs/test_create_base_text_units.py, tests/verbs/test_create_communities.py, tests/verbs/test_create_community_reports.py, tests/verbs/test_create_final_documents.py, tests/verbs/test_create_final_text_units.py, tests/verbs/test_extract_covariates.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
  - `compare_outputs(actual, expected, columns) -> None`
    - Mục đích: Compare the actual and expected dataframes, optionally specifying columns to compare.
    - Được tham chiếu bởi (xấp xỉ): tests/verbs/test_create_base_text_units.py, tests/verbs/test_create_communities.py, tests/verbs/test_create_community_reports.py, tests/verbs/test_create_final_documents.py, tests/verbs/test_create_final_text_units.py
    - Input: tham số trong chữ ký hàm ở trên.
    - Output: giá trị trả về theo annotation hoặc kết quả xử lý nghiệp vụ của hàm.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

### Thư mục con: `tests/verbs/data`

- Số file: **11**

#### File: `tests/verbs/data/communities.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/community_reports.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/covariates.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/covariates.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/documents.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/entities.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/entities.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/relationships.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/relationships.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/text_units.csv`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).

#### File: `tests/verbs/data/text_units.parquet`
- **Loại**: other
- **Vai trò**: File kiểm thử để xác thực hành vi module/liên kết tích hợp.
- **Vì sao cần file này**: là mắt xích chức năng trong pipeline/module tương ứng; thiếu file này sẽ mất khả năng tương ứng (CLI, indexing, query, test, hoặc cấu hình).
