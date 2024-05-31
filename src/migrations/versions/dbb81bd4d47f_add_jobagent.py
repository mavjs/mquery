"""add jobagent
Revision ID: dbb81bd4d47f
Revises: cbbba858deb0
Create Date: 2024-05-29 13:13:03.980030
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dbb81bd4d47f"
down_revision = "cbbba858deb0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "jobagent",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_in_progress", sa.Integer(), nullable=False),
        sa.Column("job_id", sa.Integer(), nullable=False),
        sa.Column("agent_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["agent_id"],
            ["agentgroup.id"],
        ),
        sa.ForeignKeyConstraint(
            ["job_id"],
            ["job.internal_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("jobagent")
    # ### end Alembic commands ###