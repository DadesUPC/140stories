"""empty message

Revision ID: dd02e78063e2
Revises: f8f05128a604
Create Date: 2017-09-16 19:35:13.820068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd02e78063e2'
down_revision = 'f8f05128a604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('story', 'url')
    # ### end Alembic commands ###