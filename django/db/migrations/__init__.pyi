from .migration import Migration as Migration, swappable_dependency as swappable_dependency
# XXX: from .operations import *

from .operations.fields import AddField as AddField, AlterField as AlterField, RemoveField as RemoveField, RenameField as RenameField

from .operations.models import (
    AddIndex as AddIndex, AlterIndexTogether as AlterIndexTogether, AlterModelManagers as AlterModelManagers, AlterModelOptions as AlterModelOptions,
    AlterModelTable as AlterModelTable, AlterOrderWithRespectTo as AlterOrderWithRespectTo, AlterUniqueTogether as AlterUniqueTogether, CreateModel as CreateModel,
    DeleteModel as DeleteModel, RemoveIndex as RemoveIndex, RenameModel as RenameModel,
)

from .operations.special import RunPython as RunPython
