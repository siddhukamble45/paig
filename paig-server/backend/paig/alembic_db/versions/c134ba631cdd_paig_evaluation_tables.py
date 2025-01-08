"""paig_evaluation_tables

Revision ID: c134ba631cdd
Revises: a95b604c47fb
Create Date: 2025-01-08 21:13:30.659062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import core.db_models.utils


# revision identifiers, used by Alembic.
revision: str = 'c134ba631cdd'
down_revision: Union[str, None] = 'a95b604c47fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evaluation',
    sa.Column('purpose', sa.String(), nullable=True),
    sa.Column('application_name', sa.String(length=255), nullable=False),
    sa.Column('owner', sa.String(length=255), nullable=False),
    sa.Column('application_client', sa.String(length=255), nullable=False),
    sa.Column('config', sa.String(), nullable=True),
    sa.Column('categories', sa.String(), nullable=True),
    sa.Column('custom_prompts', sa.String(), nullable=True),
    sa.Column('eval_id', sa.String(length=255), nullable=False),
    sa.Column('cumulative_result', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('passed', sa.Integer(), nullable=False),
    sa.Column('failed', sa.Integer(), nullable=False),
    sa.Column('report_id', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_evaluation_id'), 'evaluation', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_evaluation_id'), table_name='evaluation')
    op.drop_table('evaluation')
    # ### end Alembic commands ###
