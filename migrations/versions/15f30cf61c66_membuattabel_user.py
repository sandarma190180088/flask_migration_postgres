"""membuattabel user

Revision ID: 15f30cf61c66
Revises: fac7a7f8b449
Create Date: 2023-01-27 23:27:15.725564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15f30cf61c66'
down_revision = 'fac7a7f8b449'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_dataUser',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_user')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_dataUser')
    # ### end Alembic commands ###
