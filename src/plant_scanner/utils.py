from contextlib import asynccontextmanager


@asynccontextmanager
async def allocate_tensors():
    """
    Tensor memmory allocation
    """
    # code before yield
    yield