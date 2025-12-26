
try:
    views = env['ir.ui.view'].search([('model', '=', 'hr.candidate')])
    print(f"Found {len(views)} views for hr.candidate")
    for v in views:
        print(f"Checking View ID: {v.id}, Name: {v.name}, XML ID: {v.xml_id}")
        if 'birth_date' in v.arch_db:
            print(f"!!! FOUND ROGUE VIEW WITH birth_date: {v.id} !!!")
            print(v.arch_db)
            # v.unlink()
            # env.cr.commit()
            # print("Rogue view deleted.")
        else:
            print(" - Clean")
            
    # Also check if there are any other text occurrences in ir.ui.view regardless of model, just in case
    # rogue_all = env['ir.ui.view'].search([('arch_db', 'ilike', 'birth_date'), ('model', '=', 'hr.candidate')])
    # print(f"Search by content found: {len(rogue_all)}")
except Exception as e:
    print(f"Error: {e}")
